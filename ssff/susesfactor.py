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

def ingresar(nombre, apellido, fecha_n,pais ):
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
                driver.find_element(By.XPATH,'//*[@id="__box9-inner"]').send_keys("mede")
                time.sleep(2)
                ciud="Medellín"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box9-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            else:
                driver.find_element(By.XPATH,'//*[@id="__box4-arrow"]').click()
                time.sleep(2)
                ciud="Otros municipios"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box9-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            print("municipio select")
        except:
            print("error ciudad")


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
    if cont==1:
        break
    #//*[@id="main--globalSFHeader"]

    temporal()
    ingresar(nombre, apellido, fechan,pais )
    #parte1(nombre,apellido,fechan,pais,sexo,cedula)

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

        