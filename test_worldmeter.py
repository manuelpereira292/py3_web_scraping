from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

link_page = 'https://www.worldometers.info/pt/'

navegador = webdriver.Firefox()
navegador.get(link_page)

print(navegador.title)

try:
    main = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'item'))
        )
    print(main)

finally:
    navegador.quit()
