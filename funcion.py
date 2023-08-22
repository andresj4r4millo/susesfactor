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

# Función para enviar correo
def enviar_correo(cedula):
    sender_email = 'andres.jaramillo@onecontact.com.co'
    sender_password = 'Andres123,'
    receiver_email = 'andres.jaramillo8819@outlook.com'
    subject = 'Captura de pantalla'

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Agregar el cuerpo del mensaje (opcional)
    body = 'Adjunto encontrarás la captura de pantalla.'
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar la captura de pantalla
    screenshot_path = f'capturas/{cedula}.png'
    with open(screenshot_path, 'rb') as image_file:
        image_data = image_file.read()
        image = MIMEImage(image_data, name=f'{cedula}.png')
        msg.attach(image)

    # Enviar el correo
    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Correo enviado exitosamente")
    except Exception as e:
        print("Error al enviar el correo:", e)
        
#busqueda 
def buscar(anime):
    try:
        buscador=driver.find_element(By.XPATH,'//*[@id="searchInput"]')
        buscador.clear()
        buscador.send_keys(anime)
        time.sleep(2)
        buscador.send_keys(Keys.ENTER)
        time.sleep(2)
    except:
        #//*[@id="searchform"]/div/div/div[1]/input
        buscador=driver.find_element(By.XPATH,'//*[@id="searchform"]/div/div/div[1]/input')
        buscador.clear()
        buscador.send_keys(anime)
        time.sleep(2)
        buscador.send_keys(Keys.ENTER)
        time.sleep(2)


animes= {
    "la rueda": False,
    "wabi wabo xxxxllss":False,
    "la imprenta": False,
    "el papel higienico":False,
    "jojo":False,
    "wabi wabo xxxxllss":False
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
    #if 'ANIME' in driver.page_source:
    try:
        driver.find_element(By.XPATH,'//*[@id="ca-view"]/a/span')#//*[@id="ca-view"]/a/span
        time.sleep(1)
        screenshot_name = f'capturas/{i}.png'
        driver.save_screenshot(screenshot_name)
        print(f"Captura tomada y guardada en {screenshot_name}")
        print("captura")
        # Llamar a la función para enviar el correo
        enviar_correo(i)
        with open('animes encontrados.txt', 'w') as archivo:

            archivo.write(i + '\n')
        print("se encontro")
    except:
        print("no activo")
   # time.sleep(20)

    # Hacer más acciones con el navegador...

    # Cerrar el navegador
    
