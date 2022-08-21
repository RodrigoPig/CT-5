from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

link = 'https://cadastramento-demo.mercafacil.com/#/home'
cpf = '111.065.153-82'
nome = 'Gabrielly Sophia Moraes'
celular = '(62) 98751-7969'
data_nasc = '10/01/1997'
email = 'gabrielly_sophia_moraes@rogerstenis.com.br'
cep = '60426-055'
numero = '45'
senha = '123456'
confirma_senha = senha

# Acessando a pagina de cadastro PF

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

# Inserindo dados para o cadastramento

nav.find_element(By.ID,'input-42').send_keys(nome)
sleep(2)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[3]/div/div/div[1]/div/div[1]/div/div').click()
nav.find_element(By.ID,'input-46').send_keys(celular)
sleep(2)
nav.find_element(By.ID,'input-50').send_keys(email)
sleep(2)
nav.find_element(By.ID,'input-54').send_keys(data_nasc)
sleep(2)
nav.find_element(By.ID,'input-81').send_keys(cep)
sleep(2)
nav.find_element(By.ID,'input-108').send_keys(numero)
sleep(2)
nav.find_element(By.ID,'input-68').send_keys(senha)
sleep(2)
nav.find_element(By.ID,'input-72').send_keys(confirma_senha)
sleep(2)

# marcando os termos de adesão

nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[9]/div[1]').click()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div/div/div[2]/button[1]').click()
sleep(3)
nav.find_element(By.ID,'input-72').send_keys(Keys.PAGE_DOWN)
sleep(2)

# Confirmando o cadastro

nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[9]/div[2]/button[1]').click()
sleep(2)
nav.delete_all_cookies()
sleep(3)
nav.close()
