from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

'''
1 - A acessar o link de transmissão no YouTube Studio
2 - Adquirir os dados do evento/live (Nome, Horário de ínicio, chave de transmissão e canal)
3 - Passar esses dados para um template de mensagem
'''

# Configurando o webdriver do Google Chrome

'''try:
    os.system('cmd /k "cd C:\Program Files\Google\Chrome\Application"')
    os.system('cmd /k "chrome.exe --remote-debugging-port=9933"')
    os.system('cmd /k "chrome.exe --user-data-dir=Default"')
except:
    print('Erro! Não foi possível abrir o navegador')'''
os.environ['PATH'] += r'C:/SeleniumDrivers'
options = webdriver.ChromeOptions()
#options.add_experimental_option('debuggerAddress', 'localhost:9933')
options.add_argument('user-data-dir=C:/Users/Mateus/AppData/Local/Google/Chrome/User Data')
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=options)
driver.get("https://youtube.com")  
sleep(5)
