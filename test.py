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

navegador = webdriver.Firefox()
navegador.get(link_login)

campo_email = navegador.find_element_by_name('l')
campo_email.send_keys(email)
campo_passw = navegador.find_element_by_name('p')
campo_passw.send_keys(passw)
campo_passw.send_keys(Keys.RETURN)
sleep(5)
navegador.get(link_equipamentos)
sleep(5)

try:
    campo_procurar = navegador.find_element_by_css_selector('form-control.form-control-sm')
    print(campo_procurar)
    print('test1')
    campo_procurar.send_keys('58371')
    campo_procurar.send_keys(Keys.RETURN)

except:
    pass

try:
    campo_procurar = navegador.find_element_by_xpath('//label/input')
    print(campo_procurar)
    print('test2')
    campo_procurar.send_keys('58371')
    campo_procurar.send_keys(Keys.RETURN)

except:
    pass


"""
try:
    main = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    print(main.text)

except:
    navegador.quit()

"""

sleep(6)
navegador.quit()
