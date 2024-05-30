from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#Predefinições
chrome_options = Options()

arguments = ['--lang=pt-BR','--window-size=600,600','--incognito']
for argument in arguments:
    chrome_options.add_argument(argument)
'''
'''
#Add predefiniçoes exprimentais 
chrome_options.add_experimental_option('prefs', {
    #'dowload.default_directory': 'D:\\projeto\\download', # Altera o local padrão de download de arquivos
    'downlaad.directory_upgrade': True, #Notificar o google sobre essa notificação
    'profile.default_content_setting_values.notifications': 2, #Desabilita notificaçoes 
    'profile.default_content_setting_values.automatic_downloads': 1 # Permite varios Downloads  
})

#iniciando o webdriver  
driver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

#Ir até o site 
driver.get('http://facebook.com')
input('apertar tecla para sair\n')