from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager

#iniciando o webdriver  
driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Ir até o site 
driver.get('http://facebook.com')
input('apertar tecla para sair')