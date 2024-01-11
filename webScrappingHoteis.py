import openpyxl
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    # Abrindo o chrome e acessando o Booking.com
    driver = webdriver.Chrome()
    driver.get("https://www.booking.com")

    time.sleep(5)

    # Localiza o botão pelo XPath do dialog
    xpath_dialog_login = "//div[@class='abcc616ec7 cc1b961f14 c180176d40 f11eccb5e8 ff74db973c']/button[@aria-label='Ignorar informações de login.']"
    botao_dialog_login = driver.find_element(By.XPATH, xpath_dialog_login)
    # Clica no botão X para fechar o dialog
    botao_dialog_login.click()

    # Localize o campo LOCAL pelo seletor de Classe
    local_selector = "eb46370fe1"
    local_campo = driver.find_element(By.CLASS_NAME, local_selector)
    # Insira um valor no campo
    local_nome = 'Noronha'
    local_campo.send_keys(local_nome)

    # Localiza o campo DATA pelo seletor Classe
    data_selector = "a1139161bf" 
    data_campo = driver.find_element(By.CLASS_NAME, data_selector) 
    # Insira um valor no campo
    data_campo.click()


    # Localiza o elemento pelo XPath usando o atributo data-date para a Data Inicio
    xpath_data_1 = "//span[@data-date='2024-01-17']"
    elemento1 = driver.find_element(By.XPATH, xpath_data_1)
    # Execute click na data encontrada
    elemento1.click(

    
    # Localiza o elemento pelo XPath usando o atributo data-date para a Data Fim
    xpath_data_2 = "//span[@data-date='2024-01-30']"
    elemento2 = driver.find_element(By.XPATH, xpath_data_2)
    # Execute click na data encontrada
    elemento2.click()

    # Localiza o campo do tipo de Quartos
    quarto_selector = 'd777d2b248'
    quarto_elemento = driver.find_element(By.CLASS_NAME, quarto_selector)
    # Executa o click para selecionar os tipos de quarto
    quarto_elemento.click()

    # Soma 1 adulto no quarto
    adulto_selector = '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a"]'
    adulto_elemento = driver.find_element(By.XPATH, adulto_selector)
    # Executa o click para adicionar adulto
    adulto_elemento.click()

    # Encontra selector para Quantidade de Quartos
    qnt_quarto_selector = '//input[@id="no_rooms"]/following-sibling::div/button[contains(@class, "a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a")]'
    qnt_quarto_elemento = driver.find_element(By.XPATH, qnt_quarto_selector)
    #Executa o click para adicionar crianca
    qnt_quarto_elemento.click()

     
    # Soma 1 crianca no quarto
    crianca_selector = '//input[@id="group_children"]/following-sibling::div/button[contains(@class, "a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a")]'
    crianca_elemento = driver.find_element(By.XPATH, crianca_selector)
    #Executa o click para adicionar crianca
    crianca_elemento.click()

    # Encontra o seletor para Quantidade de crianças
    crianca_selector ='//select[@class="ebf4591c8e"]'
    crianca_elemento = driver.find_element(By.XPATH, crianca_selector)
    select_crianca_elemento = Select(crianca_elemento)
    select_crianca_elemento.select_by_value("2")


    pesquisar_selector = '//*[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]'
    pesquisar_selector_elemento = driver.find_element(By.XPATH, pesquisar_selector)
    # Executa o click para adicionar adulto
    pesquisar_selector_elemento.click()

    time.sleep(5)

    # Seleciona o filtro de Hotel
    filtro_hotel_selector = '//div [@data-filters-item = "ht_id:ht_id=204"]'
    filtro_hotel_elemento = driver.find_element(By.XPATH, filtro_hotel_selector)
    filtro_hotel_elemento.click()

    time.sleep(5)


    # Clica na botão para habilitar ordenações
    habilita_ordenacoes_selector = '//button[@class="a83ed08757 faefc93c6f b94d37c0c4"]'
    habilita_ordenacoes_elemento = driver.find_element(By.XPATH, habilita_ordenacoes_selector)
    habilita_ordenacoes_elemento.click()

    # Seleciona filtro de ordenação
    filtro_ordenacao_selector = '//button[@data-id = "price"]'
    filtro_ordenacao_elemento = driver.find_element(By.XPATH, filtro_ordenacao_selector)
    filtro_ordenacao_elemento.click()

    time.sleep(5)

    #workbook = openpyxl.Workbook()
    #workbook.create_sheet('lista_hoteis')
    #sheet_hoteis = workbook['lista_hoteis']
    #sheet_hoteis['A1'].value = 'Tipo_Ordenacao'
    #sheet_hoteis['B1'].value = 'Nome_Hotel'
    #sheet_hoteis['C1'].value = 'Preco'
    #sheet_hoteis['D1'].value = 'Camas'
    #sheet_hoteis['E1'].value = 'Avaliacao'

    tipo_ordenacao = 'Preço (Mais baixo para o mais alto'
    nome_hotel = driver.find_elements(By.XPATH, '//div[@data-testid="title"]')
    preco = driver.find_elements(By.XPATH, '//span [@class="f6431b446c fbfd7c1165 e84eb96b1f"]')
    avaliacao = driver.find_elements(By.XPATH, '//div[@class="a3b8729ab1 d86cee9b25"]')

    for aval in avaliacao:
        print(aval.text)


    time.sleep(10)

    # Fechar o navegador
    driver.quit()

except Exception as e:
        print(f"Ocorreu um erro: {e}")

