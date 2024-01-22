from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

try:
    # Acessar o site do Booking...

    driver = webdriver.Chrome()
    driver.get('https://www.booking.com/index.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaCCIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4Apae96wGwAIB0gIkNjRhZGVjMjMtZDZjYS00ZDRjLWI0ODktY2VlNjY2NGVhZWI02AIF4AIB&sid=6cc4d58fa099e2e5448712cd43016176&keep_landing=1&sb_price_type=total&')


    # Filtrar pesquisa

    driver.find_element(By.CLASS_NAME, 'eb46370fe1').click()
    driver.find_element(By.CLASS_NAME, 'eb46370fe1').send_keys('São Sebastião')
    driver.find_element(By.CLASS_NAME, 'f73e6603bf').click()
    teste = driver.find_element(By.CLASS_NAME, 'e1eebb6a1e ee7ec6b631')
    print(teste.find_element(By.TAG_NAME, 'h3'))
