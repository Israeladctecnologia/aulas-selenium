from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # Para poder fazer a busca pelo elemento
from selenium.webdriver.chrome.options import Options

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR','--window-size=800,600','--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'downlaad.directory_upgrade': True, #Notificar o google sobre essa notificação
        'profile.default_content_setting_values.notifications': 2, #Desabilita notificaçoes 
        'profile.default_content_setting_values.automatic_downloads': 1 # Permite varios Downloads  
    })  
    driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
botao = driver.find_element(By.ID, 'buttonalerta')
botoes= driver.find_elements(By.ID, 'buttonalerta')

# Apos o By.ID podemos usar NAME, CLASS_NAME, LINK_TEXT, XPATH - '//*[text()="ZONA DE TESTES"]

if botao is not None:
    print('botão foi encontrado')
if botoes is not None:
    print('Botoes encontrados')  # assim ele indica se foi encontrado o elemento 
input('apertar tecla para sair\n')  # Assim a página não fecha 