from notifypy import Notify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pygetwindow as gw
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from notifypy import Notify
"""
notification = Notify()
notification.title = "Cool Title"
notification.message = "Even cooler message."

notification.send()
"""
def buscar(anime):
    buscador=driver.find_element(By.XPATH,'//*[@id="searchInput"]')
    buscador.clear()
    buscador.send_keys(anime)
    time.sleep(2)
    buscador.send_keys(Keys.ENTER)
    time.sleep(2)
animes= {
    "kenichi": False,
    "boku no hero": False,
    "hajime no ippo":False,
    "jojos":False,
    "wabi wabo":False
}
driver= webdriver.Edge()
driver.maximize_window()
# Abrir una página web en el navegador
driver.get("https://www.wikipedia.org/")
time.sleep(2)
for i in animes:
    #anime=i.keys()
    #print(i)
    buscar(i)
    #/html/body/div[2]/div/div/main/ul
    if i in driver.page_source:
    #try:
        #driver.find_element(By.XPATH,'/html/body/div[2]/div/div/main/div/ul/li/a')
        time.sleep(1)
        screenshot_name = f'capturas/{i}.png'
        driver.save_screenshot(screenshot_name)
        print(f"Captura tomada y guardada en {screenshot_name}")
        print("captura")
        # Llamar a la función para enviar el correo
        #enviar_correo(i)
        notification = Notify()
        notification.title = "Cool Title"
        notification.message = "Even cooler message."

        notification.send()
        with open('animes encontrados.txt', 'w') as archivo:

            archivo.write(i + '\n')
        print("se encontro")
    else:
        print("no activo")
   # time.sleep(20)

    # Hacer más acciones con el navegador...

    # Cerrar el navegador
    
