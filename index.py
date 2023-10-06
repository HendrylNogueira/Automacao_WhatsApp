import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep


#  Abre o navegador

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com/")
sleep(5)
print('Abrindo navegador')
sleep(5)
print('Carregando')
sleep(5)
print('Processando informações')
sleep(5)
print('Navegador aberto com sucesso!')
sleep(5)
print('Abrindo o chat...')
sleep(4)

mensagem = '''Boa noite!
Segue teste de mensagem.
'''

lista_contatos = ['Eu (você)', 'Curso de WordPress', 'Teste 2', 'Teste python']

# Envia a mensagem para o primeiro contato

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()  # clica na lupa para pesquisar
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys('Eu (você)')  # digita o nome do primeiro contato
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)  # abre o chat
print('Chat aberto!')
sleep(4)

# digitar a mensagem e enviar


pyperclip.copy(mensagem)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'v')  # Cola a mensagem para enviar
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)  # pressiona enter e envia a mensagem
print('Primeira mensagem enviada com sucesso!')
sleep(4)

# logica para encontrar a caixa de texto correta

from selenium.webdriver.common.action_chains import ActionChains

elemento = ''
lista_elementos = nav.find_elements('class name', 'CzM4m')
for item in lista_elementos:
    mensagem = mensagem.replace('\n', '')
    texto = item.text.replace('\n', '')
    if mensagem in texto:
        elemento = item
        break

# caixa de texto encontrada, encaminhando mensagem

ActionChains(nav).move_to_element(elemento).perform()

elemento.find_element('class name', '_3u9t-').click()  # clica na opção da mensagem
sleep(4)
nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[3]').click()  # clica no opção encaminhar
sleep(4)
nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]').click()  # clica na seta para encaminhar
sleep(4)

# Seleciona os contatos para enviar

nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys('Curso de WordPress')  # Digitar o contato para envio
sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)  # pressiona enter
sleep(2)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys('Teste python')  # Digita o proximo contato
sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)  # pressiona enter
sleep(2)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys('Teste 2')
sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)  # pressiona enter
sleep(5)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()  # Clica em enviar
print('Mensagem enviada a todos os contatos!')

fechar = input('Finalizado com sucesso!')
