from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

link_inicial = 'https://backoffice.geocar.info'
link_empresas = 'https://backoffice.geocar.info/index.php/emp'
link_equipamentos = 'https://backoffice.geocar.info/index.php/equip'
link_cartoes = 'https://backoffice.geocar.info/index.php/card'
email = 'manuel.pereira@geocar.info'
passw = 'l3'+'xA'+'p6'+'5V'

navegador = webdriver.Firefox()
navegador.get(link_inicial)

campo_email = navegador.find_element_by_name('l')
campo_email.send_keys(email)
campo_passw = navegador.find_element_by_name('p')
campo_passw.send_keys(passw)
campo_passw.send_keys(Keys.RETURN)

sleep(5)

navegador.get(link_empresas)
sleep(5)
navegador.get(link_equipamentos)
sleep(5)
navegador.get(link_cartoes)
sleep(5)


try:
    main = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, 'main'))
    )
    print(main.text)

except:
    navegador.quit()

sleep(6)
navegador.quit()
