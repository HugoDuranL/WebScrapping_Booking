from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from conversor_ordenacao_pagina import converter_tipo_paginacao
import time
import openpyxl
from model.reserva import Reserva


def find_Element(byElement, elementName):
    # Localiza o elemento
    print(f"By element: {byElement}, finding element: {elementName}")
    element = driver.find_element(byElement, elementName)
    # Execute click na data encontrada
    element.click()

def find_ElementReturn(byElement, elementName):
    # Localiza o elemento
    print(f"By element: {byElement}, finding element: {elementName}")
    element = driver.find_element(byElement, elementName)
    return element

def loginDialog():
    # Localiza o botão pelo XPath do dialog
    find_Element(By.XPATH, "//div[@class='abcc616ec7 cc1b961f14 c180176d40 f11eccb5e8 ff74db973c']/button[@aria-label='Ignorar informações de login.']")

def getDestinoPesquisa(local_nome):
    # Localize o campo LOCAL pelo seletor de Classe
    local_campo = find_ElementReturn(By.CLASS_NAME, "eb46370fe1")
    # Insira um valor no campo
    local_campo.send_keys(local_nome)

def getDataPesquisa():
    # Localiza o campo DATA pelo seletor Classe
    find_Element(By.CLASS_NAME, "a1139161bf")

    # Localiza o elemento pelo XPath usando o atributo data-date para a Data Inicio
    find_Element(By.XPATH, "//span[@data-date='2024-01-17']")
        
    # Localiza o elemento pelo XPath usando o atributo data-date para a Data Fim
    find_Element(By.XPATH, "//span[@data-date='2024-01-30']")

def getQuartoPesquisa():
     # Localiza o campo do tipo de Quartos
    find_Element(By.CLASS_NAME, 'd777d2b248')

    # Soma 1 adulto no quarto
    find_Element(By.XPATH, '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a"]')

    # Encontra selector para Quantidade de Quartos
    find_Element(By.XPATH, '//input[@id="no_rooms"]/following-sibling::div/button[contains(@class, "a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a")]')

    # Soma 1 crianca no quarto
    find_Element(By.XPATH, '//input[@id="group_children"]/following-sibling::div/button[contains(@class, "a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a")]')

    # Encontra o seletor para Quantidade de crianças
    crianca_selector ='//select[@class="ebf4591c8e"]'
    crianca_elemento = driver.find_element(By.XPATH, crianca_selector)
    select_crianca_elemento = Select(crianca_elemento)
    select_crianca_elemento.select_by_value("2")

def camposPesquisa(local_nome):
    getDestinoPesquisa(local_nome)
    getDataPesquisa()
    getQuartoPesquisa()

def pesquisarHoteis():
    # Encontra o selector de Pesquisar e clica no botão
    find_Element(By.XPATH, '//*[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]')

def pesquisarTipoPropriedade(tipoPropriedade):
    # Seleciona o filtro de Hotel
    find_Element(By.XPATH, f'//div [@data-filters-item = "{tipoPropriedade}"]')

def ordernacaoDaPagina(ordenacaoPaginaEnum):
    # Clica na botão para habilitar ordenações
    find_Element(By.XPATH, '//button[@class="a83ed08757 faefc93c6f b94d37c0c4"]')

    # Seleciona filtro de ordenação
    find_Element(By.XPATH, f'//button[@data-id = "{ordenacaoPaginaEnum}"]')

def criacaoPlanilha():
    # Criando a planilha
    workbook = openpyxl.Workbook()
    # Criando a pagina
    workbook.create_sheet('hoteis')
    # Seleciona a pagina
    sheet_hoteis = workbook['hoteis']
    # Criando as colunas da pagina
    sheet_hoteis['A1'].value = 'Tipo da Ordenação'
    sheet_hoteis['B1'].value = 'Nome do Hotel'
    sheet_hoteis['C1'].value = 'Preço da estadia'

    return workbook, sheet_hoteis

def preenchePlanilha(workbook, sheet_hoteis):
    tipo_ordenacao = 'Preço (Mais baixo para o mais alto)'
    nome_hotel = driver.find_elements(By.XPATH, '//div[@data-testid="title"]')
    precos = driver.find_elements(By.XPATH, '//span [@class="f6431b446c fbfd7c1165 e84eb96b1f"]')

    for nome, preco in zip(nome_hotel, precos):
        sheet_hoteis.append([tipo_ordenacao, nome.text, preco.text])
        print(f'Hotel {nome.text} preco {preco.text}')

    workbook.save('hoteis.xlsx')

def teste(request: Reserva):
    try:
        # Abrindo o chrome e acessando o Booking.com
        driver = webdriver.Chrome()
        driver.get("https://www.booking.com")

        time.sleep(5)

        # Tira o dialg de login
        loginDialog()

        # Preencher campos de pesquisa
        local_nome = 'noronha'
        camposPesquisa(local_nome)

        # Pesquisar Hoteis
        pesquisarHoteis()

        time.sleep(5)

        # Pesquisar pelo tipo da Propriedade Hoteis = ht_id:ht_id=204
        tipoPropriedade = 'ht_id:ht_id=204'
        pesquisarTipoPropriedade(tipoPropriedade)

        time.sleep(5)

        # Tipo da ordernacao da Pagina dos Hoteis
        tipoPaginacao = 'Preço (mais baixo primeiro)'
        ordenacaoPaginaEnum = converter_tipo_paginacao(tipoPaginacao)
        ordernacaoDaPagina(str(ordenacaoPaginaEnum))

        time.sleep(5)

        workbook, sheet_hoteis = criacaoPlanilha()
        
        preenchePlanilha(workbook, sheet_hoteis)
        
        time.sleep(10)

        # Fechar o navegador
        driver.quit()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")



