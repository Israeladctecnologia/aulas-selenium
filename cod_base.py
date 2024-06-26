from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
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
driver.get('https://facebook.com')
input('apertar tecla para sair\n')