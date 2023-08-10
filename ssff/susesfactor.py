from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
#para el libro de exporte
import openpyxl
from unidecode import unidecode
import re
import pandas as pd
import numpy as np
from lxml import html
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import traceback
#import funciones

driver= webdriver.Edge(executable_path='msedgedriver.exe')
driver.maximize_window()
driver.implicitly_wait(4)
actions = ActionChains(driver)
workbook = openpyxl.load_workbook('SSFF.xlsx', read_only=True, data_only=True, keep_links=False, keep_vba=False)
# Seleccionar la hoja de cálculo que deseas leer
sheet = workbook['Hoja1']
######################################################################################################################################################
##########################################################  AÑADIR TRABAJADOR TEMPORAL
def temporal():
    while True:
        try:

            primer_etiqueta=driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/xweb-shellbar')
            primer_shadow_root = driver.execute_script('return arguments[0].shadowRoot', primer_etiqueta)
            segunda_etiqueta = primer_shadow_root.find_element(By.ID,"search")
            segundo_shadow_root = driver.execute_script('return arguments[0].shadowRoot', segunda_etiqueta)

            buscador = segundo_shadow_root.find_element(By.ID, "ui5wc_14-inner")
            time.sleep(1)
            buscador.send_keys("Añadir trabajador temporal")
            time.sleep(2)
            buscador.send_keys(Keys.ARROW_DOWN)
            buscador.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            buscador.send_keys(Keys.ENTER)

            print("tambien se encontro")

            time.sleep(5)
            break
        except Exception as e:

            print("No se pudo interactuar:", e)
def ssff():
    while True:
        try:
            # //*[@id="shellbar"]//header/div[1]/span
            primer_etiqueta=driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/xweb-shellbar')#//*[@id="container"]/div[1]/div/xweb-shellbar
            primer_shadow_root = driver.execute_script('return arguments[0].shadowRoot', primer_etiqueta)
            segunda_etiqueta = primer_shadow_root.find_element(By.ID,"shellbar")
            segundo_shadow_root = driver.execute_script('return arguments[0].shadowRoot', segunda_etiqueta)
            btn_inicio=segundo_shadow_root.find_element(By.XPATH, '//*[@id="shellbar"]//header/div[1]/button/span')
            btn_inicio.click()
            print("inicio")
            break
        except:
            print("boton no encontrado")

def ingresar(nombre, apellido, fecha_n,pais,cedula,fechaex,codigo_p ):
    while True:
        try:
            #NOMBRE
            driver.find_element(By.XPATH,'//*[@id="__input0-inner"]').send_keys(nombre)
            #APELLIDO
            driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys(apellido)
            break
        except:
            print("no se pudo diligenciar")
    while True:
        try:
            #FECHA NACIMIENTO
            #campofecha=driver.find_element(By.XPATH,'//*[@id="__picker0-inner"]')
            #actions.double_click(campofecha).perform()
            #campofecha.clear()
            #campofecha.send_keys(fecha_n)
            #time.sleep(1)
            #empresa
            elemento_input = driver.find_element(By.ID,"__box0-inner")
            texto="ONE CONTACT INTERNACIONAL (CA661)"
            elemento_input.send_keys("661")
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box0-popup-list-listUl"]//div[text()="{texto}"]')))
            #//*[@id="__box0-popup-list-listUl"]
            opcion.click()
            time.sleep(2)
            elemento_input.send_keys(Keys.ARROW_DOWN)
            elemento_input.send_keys(Keys.ENTER)
            time.sleep(1)#
            # PREINGRESO
            print('bien')
            break
        except:
            print('error2')
    while True:
        try:
            #//*[@id="__box1-popup"]
            #motivo=driver.find_element(By.XPATH,'//*[@id="__box1-inner"]')
            opciont="Preingreso (H10)"
            #motivo.send_keys(opciont)
            driver.find_element(By.XPATH,'//*[@id="__box1-arrow"]').click()
            #//*[@id="__box1-popup"]
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box1-popup"]//div[text()="{opciont}"]')))
            opcion.click()
            time.sleep(1)

            break
        except:
            print("error3")
    ###informacion biografica
    while True:
        try:

            driver.find_element(By.XPATH,'//*[@id="__picker1-inner"]').send_keys(fecha_n)
            time.sleep(1)
            #//*[@id="__box2-inner"]
            #PAIS

            span=driver.find_element(By.XPATH,'//*[@id="__box2-inner"]')#//*[@id="__box2-inner"]
            span.clear()
            paism=pais.lower()
            opcion_texto=paism.capitalize()
            span.send_keys(opcion_texto)
            time.sleep(2)
             # Texto de la opción que deseas seleccionar
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box2-popup-cont"]//div[text()="{opcion_texto}"]')))
            opcion.click()
            if (opcion_texto !="Colombia"):
                departamento="Otros departamentos"
            else:
                departamento="Antioquia"
            #departamento  
            driver.find_element(By.XPATH,'//*[@id="__box3-arrow"]')
            depa=driver.find_element(By.XPATH,'//*[@id="__box3-inner"]')
            depa.clear()
            depa.send_keys(departamento)
            time.sleep(1)
            opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box3-popup-cont"]//div[text()="{departamento}"]')))
            opciond.click()
            print("bien")
            break
        except:
            print("error biografico")
    while True:
        try:
            if pais=="COLOMBIA":
                driver.find_element(By.XPATH,'//*[@id="__box4-arrow"]').click()
                driver.find_element(By.XPATH,'//*[@id="__box4-inner"]').send_keys("mede")
                time.sleep(2)
                ciud="Medellín"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box4-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            else:
                driver.find_element(By.XPATH,'//*[@id="__box4-arrow"]').click()
                driver.find_element(By.XPATH,'//*[@id="__box4-inner"]').send_keys("otros")
                time.sleep(2)
                ciud="Otros municipios"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box4-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            print("municipio select")
            break
        except:
            print("error ciudad")
    if codigo_p=="si":
        while True:
            try:
                cdp=driver.find_element(By.XPATH,'//*[@id="__input6-inner"]')
            except:
                print("error al interactuar con el codigo de la persona")
    #documento
    """
    while True:
        try:
            #                            //*[@id="__input6-inner"]
            driver.find_element(By.XPATH,'//*[@id="__input6-content"]').click()
            document=driver.find_element(By.XPATH,'//*[@id="__input6-content"]')
            print(cedula)    
            document.send_keys(cedula)
            print("si")
            time.sleep(10)
            break
        except NoSuchElementException as e:
            print("error documento")
            print("mensaje: ", e)
    """
    while True:
        try:
            nom=driver.find_element(By.XPATH,'//*[@id="__input7-inner"]')
            nom.send_keys(f"{cedula}CA661")
            ### identificacion
            print("echo")
            break
        except:
            print("error nombre")
    #IDENTIFICACION
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__box5-arrow"]').click()
            option="Colombia"
            opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box5-popup-cont"]//div[text()="{option}"]')))
            
            opciond.click()
            #tipo documento
            cc="#"
            driver.find_element(By.XPATH,'//*[@id="__box6-arrow"]').click()
            if pais=="COLOMBIA":
                cc="Cédula de ciudadanía"
            elif pais=="VENEZUELA":
                cc="Cédula de Extranjeria"
            else:
                cc="Pasaporte"
            document=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box6-popup-cont"]//div[text()="{cc}"]')))
            document.click()
            #documento
            cd=driver.find_element(By.XPATH,'//*[@id="__input10-inner"]')
            actions.double_click(cd).perform()
            cd.send_keys(cedula)
            #fecha expedicion
            fx=driver.find_element(By.XPATH,'//*[@id="__picker2-inner"]')
            fx.send_keys(fechaex)
            ##departamento de expedicion
            exp="Antioquia"
            driver.find_element(By.XPATH,'//*[@id="__box8-arrow"]').click()
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box8-popup-cont"]//div[text()="{exp}"]')))
            opcionx.click()
            #//*[@id="__box8-popup-cont"]
            #Antioquia
            #nombre de usuario
            #//*[@id="__input26-inner"]

            print("listo a envio")
            break
            #time.sleep(20)


        except:
            print("datos erroneos")
            



####################################################################################################################################################3
#######################################################################  FORMATO DE FECHA    ############################################################
def formatof(fechas):
    fechas = fecha.split("/")
    fechan = "".join(fechas)
    formato=fechan.split(" ")
    lafecha=formato[0]
    fechas=lafecha.split("-")
    fecha_n="".join(fechas)
    return fecha_n


##################################################INGRESAR#############################
def iniciar_sesion():
    while True:
        try:
            driver.get("https://performancemanager8.successfactors.com/login?bplte_logout=1&company=comunicaci&_s.crb=VG1RqGoWUmkzkcagqGY%252fybzahzatv77ql1k8j0nbZ2E%253d#/login")

            driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys("EC7061B")
            driver.find_element(By.XPATH,'//*[@id="__input2-inner"]').send_keys("Onecont2024*")
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="__button2-content"]').click()
            time.sleep(4)
            print('adentro')
            time.sleep(3)
            break
        except:
            print("a")

iniciar_sesion()

cont=0
for index, row in enumerate(sheet.iter_rows(values_only=True), start=1):
    if index==1:
        continue
    cedula=str(row[0])
    fecha_ex=str(row[1])
    fecha=str(row[2])
    pais=str(row[3])
    nombre=str(row[4])
    apellido=str(row[5])
    campaña=str(row[6])
    semilla=str(row[7])
    celular=str(row[8])
    correo=str(row[9])
    correo_corporativo=str(row[10])
    direccion=str(row[11])
    barrio=str(row[12])
    preingreso=str(row[13])
    ingreso=str(row[14])
    rm=str(row[15])
    lider_virtual=str(row[16])
    estado=str(row[17])
    observaciones=str(row[18])
    fechan=formatof(fecha)
    fechaex=formatof(fecha_ex)
    sexo="FEMENINO"
    estadoc="CASADO"
    time.sleep(2)


    #//*[@id="main--globalSFHeader"]
    while True:
        temporal()
        #ssff()
        time.sleep(1)
        #driver.get("https://performancemanager8.successfactors.com/sf/home?bplte_company=comunicaci&_s.crb=2TUciEoM%2b9O44AcjHb01h2aVK7SLjpZl13QK2%2foTuqs%3d")
        ingresar(nombre, apellido, fechan,pais,cedula,fechaex,'no' )
        #time.sleep(20)
        continuar=driver.find_element(By.XPATH,'//*[@id="__button19-BDI-content"]')
        continuar.click()
        ignorar=driver.find_element(By.XPATH,'//*[@id="__button23-inner"]')
        time.sleep(2)
        ignorar.click()#
        time.sleep(1)
        ingresar(nombre, apellido, fechan,pais,cedula,fechaex,'no' )
        driver.get("https://performancemanager8.successfactors.com/sf/home?bplte_company=comunicaci&_s.crb=2TUciEoM%2b9O44AcjHb01h2aVK7SLjpZl13QK2%2foTuqs%3d")
        


    """
    agregar()
    parte1(nombre,apellido,fechan,pais,sexo,cedula)
    parte2(fechaex,pais,cedula)
    time.sleep(6)
    cont+=1
    #driver.find_element(By.XPATH,'//*[@id="ui5wc_8-inner"]').send_keys("añadir")
    """

print("terminao")




############################################################################################
################INGRESO

        