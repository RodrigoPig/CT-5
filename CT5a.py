from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'https://cadastramento-demo.mercafacil.com/#/home'
cpf = '111.065.153-82'
senha = '123456'

nav = webdriver.Chrome()
nav.get(link)
nav.maximize_window()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/section/div/div[2]/button').click()
sleep(3)
nav.find_element(By.ID,'input-19').send_keys(cpf)
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div[2]/div/div/div[2]/button').click()
sleep(3)

# verificando as informações cadastradas

nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div[1]/div[2]/div/div[2]/button[2]').click()
sleep(2)
nav.find_element(By.ID,'input-38').send_keys(senha)
sleep(2)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div[1]/div[2]/div/div[2]/div[3]/button').click()
sleep(3)

# Fechando a pagina

nav.delete_all_cookies()
sleep(3)
nav.close()
