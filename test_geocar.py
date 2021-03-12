from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

link_login = 'https://backoffice.geocar.info'
email = 'manuel.pereira@geocar.info'
passw = 'l3'+'xA'+'p6'+'5V'
link_inicial = 'https://backoffice.geocar.info/index.php/dash'
link_empresas = 'https://backoffice.geocar.info/index.php/emp'
link_equipamentos = 'https://backoffice.geocar.info/index.php/equip'
link_cartoes = 'https://backoffice.geocar.info/index.php/card'
veiculo = '59-DA-69'

navegador = webdriver.Firefox()
navegador.get(link_login)

campo_email = navegador.find_element_by_name('l')
campo_email.clear()
campo_email.send_keys(email)
campo_passw = navegador.find_element_by_name('p')
campo_passw.clear()
campo_passw.send_keys(passw)
campo_passw.send_keys(Keys.RETURN)

navegador.get(link_equipamentos)

def todos():
    try:
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.NAME,'t_equips_length'))).send_keys('t')
        print('OK - todos')

    except:
        print('ER - todos')
        

def procurar():
    try:
        procurar = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//label/input')))
        procurar.clear()
        procurar.send_keys(veiculo)
        print('OK - procurar')

    except:
        print('ER - procurar')


def mostar():
    try:
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'custom-control-label'))).click()
        print('OK - mostrar')

    except:
        print('ER - mostrar')

todos()
mostar()
procurar()

sleep(5)

navegador.quit()