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

driver= webdriver.Edge(executable_path='msedgedriver.exe')
workbook = openpyxl.load_workbook('SSFF.xlsx', read_only=True, data_only=True, keep_links=False, keep_vba=False)
# Seleccionar la hoja de cálculo que deseas leer
sheet = workbook['Hoja1']
def formatof(fechas):
    fechas = fecha.split("/")
    fechan = "".join(fechas)
    formato=fechan.split(" ")
    lafecha=formato[0]
    fechas=lafecha.split("-")
    fecha_n="".join(fechas)
    return fecha_n
def parte1(nombre,apellido,fecha_n,pais,sexo,cedula):
    cone=0
    while cone==0:
        try:
            
            #NOMBRE
            driver.find_element(By.XPATH,'//*[@id="__input0-inner"]').send_keys(nombre)
            #APELLIDO
            driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys(apellido)
            #FECHA NACIMIENTO
            cone +=1
            driver.find_element(By.XPATH,'//*[@id="__picker3-inner"]').send_keys(fecha_n)
            time.sleep(1)

            time.Sleep(4)
            print("fecha")
            break
        except:
            print("nod")
            continue
    #PAIS
  
    cone=0
    while True:
        try:
            cone +=1
            time.sleep(1)

            span=driver.find_element(By.XPATH,'//*[@id="__box7-arrow"]')
            span.click()
            paism=pais.lower()
            opcion_texto=paism.capitalize()
             # Texto de la opción que deseas seleccionar
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box7-popup-cont"]//div[text()="{opcion_texto}"]')))
            opcion.click()
            break
        except Exception as e:
            cone += 1
            print("Error:", e)
            traceback.print_exc()
            continue
    #trato
    
    while True:
        try:
            trato=driver.find_element(By.XPATH,'//*[@id="__box6-arrow"]')
            trato.click()
            #//*[@id="__box6-popup-list-listUl"]
            if sexo=="MASCULINO":
                opctrato="Sr."
            else:
                opctrato="Sra."
            opciont = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box6-popup-cont"]//div[text()="{opctrato}"]')))
            opciont.click()
            print("sr")
            time.sleep(5)
            break
        except:
            print("error trato")
    

   
    ###departamento
    
    while True:
        try:
            depart=driver.find_element(By.XPATH,'//*[@id="__box8-content"]/div')
            depart.click()
            if pais!="COLOMBIA":

                depat="Otros departamentos"
                driver.find_element(By.XPATH,'//*[@id="__box8-inner"]').send_keys("otros")
            else:
                depat="Antioquia"

            opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box8-popup-cont"]//div[text()="{depat}"]')))
            opciond.click()
            break
        except:
            print("error departamento")
    ##ciudad 
    while True:
        try:
            
            if pais=="COLOMBIA":
                driver.find_element(By.XPATH,'//*[@id="__box9-arrow"]').click()
                driver.find_element(By.XPATH,'//*[@id="__box9-inner"]').send_keys("mede")
                time.sleep(2)
                ciud="Medellín"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box9-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            else:
                driver.find_element(By.XPATH,'//*[@id="__box9-arrow"]').click()
                time.sleep(2)
                ciud="Otros municipios"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box9-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            print("municipio select")
            time.sleep(2)
            break

            #Otros municipios
            #Medellín
        except:
            #
            print("departamento none")
    ##NOMBRE DE USUARIO 
    while True:
        try:
            usu=driver.find_element(By.XPATH,'//*[@id="__input8-inner"]')
            usu.clear()
            cadena=str(cedula+"CA661")
            usu.send_keys(cadena)
            print("usuario digitado")
            break
        except:
            print("error user")

def parte2(fechaex,pais,cedula):
    driver.find_element(By.XPATH,'//*[@id="__button26-content"]').click()
    #documento identificacion
    #pais
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__box10-arrow"]').click()
            #//*[@id="__box10-popup"]
            p="Colombia"
            opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box10-popup"]//div[text()="{p}"]')))
            opciond.click()
            print("pais document")
            time.sleep(4)
            break
        except:
            print("error paisd")
    #tipo
    while True:
        try:
            cc="#"
            driver.find_element(By.XPATH,'//*[@id="__box11-arrow"]').click()
            if pais=="COLOMBIA":
                cc="Cédula de ciudadanía"
            elif pais=="VENEZUELA":
                cc="Cédula de Extranjeria"
            else:
                cc="Pasaporte"
            #//*[@id="__box11-popup"]
            time.sleep(2)
            document=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box11-popup"]//div[text()="{cc}"]')))
            document.click()
            time.sleep(1)
            #documento numero
            n_id=driver.find_element(By.XPATH,'//*[@id="__input11-inner"]')
            n_id.clear()
            n_id.send_keys(cedula)
            #primario
            driver.find_element(By.XPATH,'//*[@id="__box12-arrow"]').click()
            time.sleep(1)
            #//*[@id="__box12-popup"]
            p="Sí"
            time.sleep(1)
            primary=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box12-popup"]//div[text()="{p}"]')))
            primary.click()
            driver.find_element(By.XPATH,'//*[@id="__picker4-inner"]').clear()
            driver.find_element(By.XPATH,'//*[@id="__picker4-inner"]').send_keys(fechaex)
            #DEPARTAMENTO EXPEDICION
            driver.find_element(By.XPATH,'//*[@id="__box13-arrow"]').click()
            dep="Antioquia"
            time.sleep(2)
            #//*[@id="__box13-popup"]
            dep_ex=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box13-popup"]//div[text()="{dep}"]')))
            dep_ex.click()
            break
        except:
            print("error tipo")
    while True:
        try:
                        #municipio o ciudad de expedicion //*[@id="__box14-arrow"]
            
            
            if pais=="COLOMBIA":
                dep_x="Medellín"
            else:
                dep_x="Otros Ciudades / Municipios"
            #driver.find_element(By.XPATH,'//*[@id="__box14-arrow"]').click()
            driver.find_element(By.XPATH,'//*[@id="__box14-inner"]').click()
            driver.find_element(By.XPATH,'//*[@id="__box14-inner"]').send_keys(dep_x)
            time.sleep(1)
            depaex=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box14-popup"]//div[text()="{dep_x}"]')))
            depaex.click()
            print("tipo ide")
            time.sleep(20)
        except Exception as e:
            print("Error:", e)



def informacion_personal(sexo,estado,pais):
    while True:
        try:
            #GENERO#
            driver.find_element(By.XPTH,'//*[@id="__box15-arrow"]').click()
            if sexo=="MASCULINO":
                sex="Hombre"
            else:
                sex="Mujer"
            #//*[@id="__box15-popup"]

            genero=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box15-popup"]//div[text()="{sex}"]')))
            genero.click()
            #estado civil //*[@id="__box16-arrow"]
            driver.find_element(By.XPATH,'//*[@id="__box16-arrow"]').click()
            time.sleep(1)
            #//*[@id="__box16-popup-cont"]
            if estado=="CASADO":
                est="Casado/a"
            elif estado=="VIUDO":
                est="viudo/a"
            else:
                est="Soltero/a"
                
            estado=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box16-popup-cont"]//div[text()="{est}"]')))
            estado.click()
            #nacionalidad
            driver.find_element(By.XPATH,'//*[@id="__box17-arrow"]').click()
            paism=pais.lower()
            opcionp=paism.capitalize()
            try:
                driver.find_element(By.XPATH,'//*[@id="__box17-inner"]').send_keys(opcionp)
                nacionalidad=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box15-popup"]//div[text()="{opcionp}"]')))
                nacionalidad.click()
            except:
                opcionp='Colombia'
                driver.find_element(By.XPATH,'//*[@id="__box17-inner"]').send_keys(opcionp)
                nacionalidad=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box15-popup"]//div[text()="{opcionp}"]')))
                nacionalidad.click()
            #lengua nativa
            driver.find_element(By.XPATH,'//*[@id="__box17-arrow"]').click()
            driver.find_element(By.XPATH,'//*[@id="__box19-inner"]').send_keys("espa")
            time.sleep(2)
            #//*[@id="__box19-popup-cont"]
            lengua=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box19-popup-cont"]//div[text()="Español"]')))
            lengua.click()
            



        except:
            print("parte2")




    
def agregar():
    time.sleep(1)

    while True:
        try:
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/section/ul/li[5]/ui5-busy-indicator/a').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="__xmlview0--newHireButton-inner"]').click()
            time.sleep(5)#//*[@id="__xmlview0--newHireButton-img"]
            #elemento_input = driver.find_element(By.XPATH, '//*[@id="__box0-inner"]')
            elemento_input = driver.find_element(By.ID,"__box0-inner")
            elemento_input.click()
            elemento_input.send_keys("661")
            time.sleep(2)
            elemento_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            elemento_input.send_keys(Keys.ENTER)
            time.sleep(1)#
            break
        except:
            print("Error 661")
            continue

        ##2
    while True:
        try:
            #coso=driver.find_element(By.XPATH, '//*[@id="__box1-inner"]')
            coso=driver.find_element(By.ID,"__box1-inner")
            coso.send_keys("Nueva")
            time.sleep(2)
            coso.send_keys(Keys.ARROW_DOWN)
            coso.send_keys(Keys.ARROW_DOWN)
            coso.send_keys(Keys.ARROW_DOWN)
            coso.send_keys(Keys.ENTER)
            print("Encontrado")
            break
        except:
            print("Error contratacion")
            continue

    ##3
    while True:
        try:
            desplegar=driver.find_element(By.ID, "__box2-inner")
            #desplegar=driver.find_element(By.XPATH, '//*[@id="__box2-inner"]')
            desplegar.send_keys("Contratación Claro")
            time.sleep(3)
            desplegar.send_keys(Keys.ARROW_DOWN)
            desplegar.send_keys(Keys.ENTER)
            time.sleep(5)
            break
        except:
            print("Error contratacion")

    driver.find_element(By.XPATH,'//*[@id="__button1-content"]').click()

driver.get("https://performancemanager8.successfactors.com/login?bplte_logout=1&company=comunicaci&_s.crb=VG1RqGoWUmkzkcagqGY%252fybzahzatv77ql1k8j0nbZ2E%253d#/login")
# Iterar sobre las filas en la hoja de cálculo
#INGRESAR
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys("EC7061B")
        driver.find_element(By.XPATH,'//*[@id="__input2-inner"]').send_keys("Onecont2024*")
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="__button2-content"]').click()
        time.sleep(4)
        print('adentro')
        break
    except:
        print("a")
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
    time.sleep(4)
    if cont==1:
        break

    agregar()
    parte1(nombre,apellido,fechan,pais,sexo,cedula)
    parte2(fechaex,pais,cedula)
    time.sleep(6)
    cont+=1
    #driver.find_element(By.XPATH,'//*[@id="ui5wc_8-inner"]').send_keys("añadir")
print("terminao")