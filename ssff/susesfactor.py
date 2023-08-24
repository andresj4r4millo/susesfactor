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
from datetime import datetime
from dateutil.relativedelta import relativedelta
from notifypy import Notify
import os
from datetime import datetime
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
def temporal(texto):
    while True:
        try:

            primer_etiqueta=driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/xweb-shellbar')#//*[@id="renderTopNavSFHeader"]/xweb-shellbar
            primer_shadow_root = driver.execute_script('return arguments[0].shadowRoot', primer_etiqueta)
            segunda_etiqueta = primer_shadow_root.find_element(By.ID,"search")
            segundo_shadow_root = driver.execute_script('return arguments[0].shadowRoot', segunda_etiqueta)

            buscador = segundo_shadow_root.find_element(By.ID, "ui5wc_14-inner")
            time.sleep(1)
            buscador.send_keys(texto)
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
def temporal_intro(texto):
    while True:
        try:

            primer_etiqueta=driver.find_element(By.XPATH, '//*[@id="renderTopNavSFHeader"]/xweb-shellbar')#//*[@id="renderTopNavSFHeader"]/xweb-shellbar
            primer_shadow_root = driver.execute_script('return arguments[0].shadowRoot', primer_etiqueta)
            segunda_etiqueta = primer_shadow_root.find_element(By.ID,"search")
            segundo_shadow_root = driver.execute_script('return arguments[0].shadowRoot', segunda_etiqueta)

            buscador = segundo_shadow_root.find_element(By.ID, "ui5wc_8-inner")#//*[@id="ui5wc_8-inner"]
            time.sleep(1)
            buscador.send_keys(texto)
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
            btn_inicio=segundo_shadow_root.find_element(By.XPATH, '//*[@id="shellbar"]//header/div[1]/span')
            btn_inicio.click()
            print("inicio")
            break
        except:
            print("boton no encontrado")

def ingresar(nombre, apellido, fecha_naci,pais,cedula,fecha_expedicion):
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

            driver.find_element(By.XPATH,'//*[@id="__picker1-inner"]').send_keys(fecha_naci)
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
                driver.find_element(By.XPATH,'//*[@id="__box4-inner"]').clear()
                driver.find_element(By.XPATH,'//*[@id="__box4-inner"]').send_keys("mede")
                time.sleep(1)
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
            fx.send_keys(fecha_expedicion)
            ##departamento de expedicion
            exp="Antioquia"
            driver.find_element(By.XPATH,'//*[@id="__box8-arrow"]').click()
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box8-popup-cont"]//div[text()="{exp}"]')))
            opcionx.click()
            #//*[@id="__box8-popup-cont"]
            #Antioquia
            #nombre de usuario
            #//*[@id="__input26-inner"]


            continuar=driver.find_element(By.XPATH,'//*[@id="__button19-BDI-content"]')
            continuar.click()
            time.sleep(4)
            if 'Tipo de Documento es obligatorio' in driver.page_source:
                driver.find_element(By.XPATH,'//*[@id="__mbox-btn-1-BDI-content"]').click()
                continue
            try:
                ventana_e=driver.find_element(By.XPATH,'//*[@id="UserSearchResult--userSearchDialog-cont"]')#//*[@id="UserSearchResult--userSearchDialog"]
                if "activo" in ventana_e.text.lower():
                    # Configura la carpeta de capturas de video
                    driver.execute_script("arguments[0].style.zoom='50%';", ventana_e)
                    carpeta_capturas = "capturas"
                    if not os.path.exists(carpeta_capturas):
                        os.makedirs(carpeta_capturas)
                    print("preparando navegador para captura")
                    

                    screenshot_name = f'capturas/{cedula}.png'
                    driver.save_screenshot(screenshot_name)
                    #ignorar
                    driver.execute_script("arguments[0].style.zoom='100%';", ventana_e)
                    
                    time.sleep(2)
                    return "activo"
                elif "cesado" in ventana_e.text.lower():
                    texto_ventana = ventana_e.text.lower() 
                    if "cesado" in texto_ventana:
                        # Utilizar una expresión regular para buscar la fecha después de "cesado"
                        patron_fecha = r'cesado el(\d{1,2}/\d{1,2}/\d{4})'  # Patrón para encontrar una fecha en formato dd/mm/yyyy después de "cesado"
                        fecha_coincidencia = re.search(patron_fecha, texto_ventana)

                        if fecha_coincidencia:
                            fecha = fecha_coincidencia.group(1)  # Obtener la fecha encontrada
                            print(f"La fecha después de 'cesado' es: {fecha}")
                        else:
                            print("No se encontró una fecha después de 'cesado'")
                    print("a")

                time.sleep(20)
            except:
                return "añadir"
            
            """
            if 'Activo' in driver.page_source:
                screenshot_name = f'capturas/{cedula}.png'
                driver.save_screenshot(screenshot_name)
                return "activo"
                
            try:
                #aceptar correspondencia 
                #//*[@id="__button23-BDI-content"]
                #cerrar
                #//*[@id="__mbox-btn-0"]

                driver.find_element(By.XPATH,'//*[@id="__mbox-btn-0-BDI-content"]').click()
            except:   
                print("listo a envio")

                #time.sleep(20)

                try:
                    driver.find_element(By.XPATH,'//*[@id="__button25-BDI-content"]')
                    try:
                        ignorar=driver.find_element(By.XPATH,'//*[@id="__button23-inner"]')
                        ignorar.click()#
                        print("aceptar")
                        return "aceptar"
                    except:
                        driver.find_element(By.XPATH,'//*[@id="__button25-BDI-content"]').click()
                        print("ignorar")
                        return "ignorar"
                except:
                    try:
                        cor=driver.find_element(By.XPATH,'//*[@id="__input15-inner"]')
                        print("añadir")
                        cor.click()
                        return "añadir"
                    except:
                        continue
            """
        except:
            print("datos erroneos")
            

##################################################################################################
def ingresar2(nombre, apellido, fecha_naci,pais,cedula,fecha_expedicion,codigo_p ):
    while True:
        try:
            #NOMBRE
            driver.find_element(By.XPATH,'//*[@id="__input13-inner"]').clear
            driver.find_element(By.XPATH,'//*[@id="__input13-inner"]').send_keys(nombre)
            #APELLIDO
            driver.find_element(By.XPATH,'//*[@id="__input14-inner"]').clear()
            driver.find_element(By.XPATH,'//*[@id="__input14-inner"]').send_keys(apellido)
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
            elemento_input = driver.find_element(By.ID,"__box10-inner")
            texto="ONE CONTACT INTERNACIONAL (CA661)"
            elemento_input.send_keys("661")
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box10-popup-list"]//div[text()="{texto}"]')))
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
            driver.find_element(By.XPATH,'//*[@id="__box11-arrow"]').click()
            #//*[@id="__box1-popup"]
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box11-popup-list-listUl"]//div[text()="{opciont}"]')))
            opcion.click()
            time.sleep(1)

            break
        except:
            print("error3")
    ###informacion biografica
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__picker4-inner"]').clear()         
            driver.find_element(By.XPATH,'//*[@id="__picker4-inner"]').send_keys(fecha_naci)
            time.sleep(1)
            #//*[@id="__box2-inner"]
            #PAIS     //*[@id="__input20-inner"]

            span=driver.find_element(By.XPATH,'//*[@id="__box12-inner"]')#//*[@id="__box2-inner"]
            span.clear()
            paism=pais.lower()
            opcion_texto=paism.capitalize()
            span.send_keys(opcion_texto)
            #desplegar opciones
            driver.find_element(By.XPATH,'//*[@id="__box12-arrow"]').click()
            time.sleep(2)
             # Texto de la opción que deseas seleccionar
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box12-popup-cont"]//div[text()="{opcion_texto}"]')))
            opcion.click()
            if (opcion_texto !="Colombia"):
                departamento="Otros departamentos"
            else:
                departamento="Antioquia"
            #departamento  
            
            depa=driver.find_element(By.XPATH,'//*[@id="__box13-inner"]')
            depa.clear()
            depa.send_keys(departamento)
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="__box13-arrow"]').click()
            opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box13-popup-cont"]//div[text()="{departamento}"]')))
            opciond.click()
            print("bien")
            break
        except:
            print("error biografico")
    while True:
        try:
            if pais=="COLOMBIA":
                driver.find_element(By.XPATH,'//*[@id="__box14-arrow"]').click()
                
                ciud=driver.find_element(By.XPATH,'//*[@id="__box14-inner"]')
                actions.double_click(ciud).perform()
                ciud.send_keys("mede")
                time.sleep(2)
                ciud="Medellín"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box14-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            else:
                driver.find_element(By.XPATH,'//*[@id="__box14-arrow"]').click()
                driver.find_element(By.XPATH,'//*[@id="__box14-arrow"]').send_keys("otros")
                time.sleep(2)
                ciud="Otros municipios"
                opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box14-popup-cont"]//div[text()="{ciud}"]')))
                opciond.click()
            print("municipio select")
            break
        except:
            print("error ciudad")
    if codigo_p=="si":
        while True:
            try:
                cdp=driver.find_element(By.XPATH,'//*[@id="__input20-inner"]')
                actions.double_click(cdp).perform()
                cdp.send_keys(f"{cedula}CA")
                break
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
            nom=driver.find_element(By.XPATH,'//*[@id="__input20-inner"]')
            nom.clear()
            nom.send_keys(f"{cedula}CA")
            ### identificacion
            print("echo")
            break
        except:
            print("error nombre")
    #IDENTIFICACION
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__box15-arrow"]').click()
            option="Colombia"
            opciond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box15-popup-cont"]//div[text()="{option}"]')))
            
            opciond.click()
            #tipo documento
            cc="#"
            driver.find_element(By.XPATH,'//*[@id="__box16-arrow"]').click()
            if pais=="COLOMBIA":
                cc="Cédula de ciudadanía"
            elif pais=="VENEZUELA":
                cc="Cédula de Extranjeria"
            else:
                cc="Pasaporte"
            document=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box16-popup-cont"]//div[text()="{cc}"]')))
            document.click()
            #documento
            cd=driver.find_element(By.XPATH,'//*[@id="__input23-inner"]')
            cd.clear()
            cd.send_keys(cedula)
            #fecha expedicion
            fx=driver.find_element(By.XPATH,'//*[@id="__picker5-inner"]')
            fx.clear()
            fx.send_keys(fecha_expedicion)
            ##departamento de expedicion
            exp="Antioquia"
            driver.find_element(By.XPATH,'//*[@id="__box18-arrow"]').click()
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box18-popup-cont"]//div[text()="{exp}"]')))
            opcionx.click()
            #//*[@id="__box8-popup-cont"]
            #Antioquia
            #nombre de usuario
            #//*[@id="__input26-inner"]
            driver.find_element(By.XPATH,'//*[@id="__button38-BDI-content"]').click()
            print("listo a envio")
            time.sleep(20)
            break
            #


        except:
            print("datos erroneos")
def info_asignacion(campaña):
    while True:
        try:
            posicion=driver.find_element(By.XPATH,'//*[@id="__box17-inner"]')
            posicion.send_keys("porta")
            opc="#"
            if campaña=="PORTA OUT":
                opc="ASESOR PORTA OUT TMK ALIADO (30031644)"
            elif campaña=="MIGRA OUT":
                opc="ASESOR MIGRA OUT TMK ALIADO (30031645)"
            
        except:
            print("err.position")
#########################################################################################################################################################
##########################################FUNCION CORREO Y  TELEFONO
def correo_tel_2(correo_corporativo,celular,correo):
    #correo
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__box19-arrow"]').click()
            tc="Corporativo"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box19-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            correoc=driver.find_element(By.XPATH,'//*[@id="__input28-inner"]')
            actions.double_click(correoc).perform()
            correoc.send_keys(correo_corporativo)
            driver.find_element(By.XPATH,'//*[@id="__box20-arrow"]').click()
            tc="Sí"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box20-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            #añadir o añadido
            cp=driver.find_element(By.XPATH,'//*[@id="__input31-inner"]')
            cp.clear()
            cp.send_keys(correo)
                
            driver.find_element(By.XPATH,'//*[@id="__box21-arrow"]').click()
            #//*[@id="__box21-popup-cont"]
            tc="Personal"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box21-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
                
            driver.find_element(By.XPATH,'//*[@id="__box22-arrow"]').clik()
            tc="No"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box22-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            break
        except:
            print(correo)


#############
####################
#######################
############################
################################
#####################################

def correo_telefono(correo_corporativo,semilla,celular,correo):
    #correo
    while True:
        try:
            #//*[@id="__input28-inner"]
            driver.find_element(By.XPATH,'//*[@id="__input15-inner"]').clear()
            driver.find_element(By.XPATH,'//*[@id="__input15-inner"]').send_keys(correo)
            
            #añadir 
            driver.find_element(By.XPATH,'//*[@id="__button35-inner"]').click()
            time.sleep(1)
            #tipo
            driver.find_element(By.XPATH,'//*[@id="__box13-arrow"]').click()
            #
            tc="Personal"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box13-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            driver.find_element(By.XPATH,'//*[@id="__input21-inner"]').clear()
            driver.find_element(By.XPATH,'//*[@id="__input21-inner"]').send_keys(correo_corporativo)
            driver.find_element(By.XPATH,'//*[@id="__box14-arrow"]').click()
            #
            pr="No"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box14-popup-cont"]//div[text()="{pr}"]')))
            opcionx.click()
            break
        except:
            print(correo)
        #telefono
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__box11-arrow"]').click()
            tc="Corporativo"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box11-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            tel=driver.find_element(By.XPATH,'//*[@id="__input18-inner"]')
            tel.clear()
            tel.send_keys(celular)
            driver.find_element(By.XPATH,'//*[@id="__box12-arrow"]').click()#//*[@id="__box24-arrow"]
            tf="Sí"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box12-popup-cont"]//div[text()="{tf}"]')))
            opcionx.click()
            #añadido #//*[@id="__button37-content"]
            driver.find_element(By.XPATH,'//*[@id="__button37-content"]').click()
            ###
            driver.find_element(By.XPATH,'//*[@id="__box17-arrow"]').click()
            tc="Personal"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box17-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            tel2=driver.find_element(By.XPATH,'//*[@id="__input27-inner"]')
            tel2.clear()
            tel2.send_keys(celular)
            driver.find_element(By.XPATH,'//*[@id="__box18-arrow"]').click()#//*[@id="__box26-arrow"]
            tf="No"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box18-popup-cont"]//div[text()="{tf}"]')))
            opcionx.click()
            driver.find_element(By.XPATH,'//*[@id="__button33-BDI-content"]').click()
            time.sleep(2)
            break
        except:
            print(celular)


def asignacion(nombre,apellido,fecha_ft,campaña):
    while True:
        try:
            #posicion
            
            driver.find_element(By.XPATH,'//*[@id="__box21-arrow"]').click()
            pt=driver.find_element(By.XPATH,'//*[@id="__box21-inner"]')
            puesto="ASESOR ADICIONALES AUTOGENERACION TMK ALIADO (30031651)"
            if campaña=="HOGAR OUT":
                puesto="ASESOR HOGAR OUT TMK ALIADO (30031640)"
                pt.send_keys("hogar")
            elif campaña=="PORTABILIDAD OUT":
                puesto="ASESOR PORTA OUT TMK ALIADO (30031644)"
                pt.send_keys("porta")
            elif campaña=="MIGRACION OUT":
                pt.send_keys("migra")
                puesto="ASESOR MIGRA OUT TMK ALIADO (30031645)"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box21-popup-cont"]//div[text()="{puesto}"]')))
            opcionx.click()
            #direccion
            driver.find_element(By.XPATH,'//*[@id="__box23-arrow"]').click()
            time.sleep(3)
            #ubicacion
            driver.find_element(By.XPATH,'//*[@id="__box25-arrow"]').click()
            ubicacion="SEDE ALIADO (6100210)"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box25-popup-cont"]//div[text()="{ubicacion}"]')))
            opcionx.click()
            print("ya casi")

            driver.find_element(By.XPATH,'//*[@id="__button56-BDI-content"]').click()
            break
        except:
            print("error de asignacion  ")
    ### work order
    while True:
        try:
            # fecha fin 2 meses
            FF=driver.find_element(By.XPATH,'//*[@id="__picker7-inner"]')#//*[@id="__picker7-inner"]

            FF.send_keys(fecha_ft)
            nombrec=(f"{nombre} {apellido}")
            cd=driver.find_element(By.XPATH,'//*[@id="__input51-inner"]')
            cd.clear()
            cd.send_keys(cedula)
            #
            nom=driver.find_element(By.XPATH,'//*[@id="__input52-inner"]')
            nom.clear()
            nom.send_keys(nombrec)

            #GESTOR INFORMACION ALIADO ONE CONTACT INTERNACIONAL
            dueño=driver.find_element(By.XPATH,'//*[@id="__box35-inner"]')
            dueño.clear()
            dueño.send_keys("GESTOR")#
            dueno="GESTOR INFORMACION ALIADO ONE CONTACT INTERNACIONAL"
            time.sleep(2)
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box35-popup-cont"]//div[text()="{dueno}"]')))
            opcionx.click()

            #proveedor
            driver.find_element(By.XPATH,'//*[@id="__box36-arrow"]').click()
            #CA661
            prov=driver.find_element(By.XPATH,'//*[@id="__box36-inner"]')
            prov.clear()

            prov.send_keys("CA661")
            provedor="CA661 (ONE CONTACT INTERNACIONAL)"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box36-popup-cont"]//div[text()="{provedor}"]')))
            opcionx.click()
            
            #fechaf.clear()
            print("asignado")
            #continuar
            time.sleep(2)
            driver.find_element(By.XPATH,'//*[@id="__button63-BDI-content"]').click()
            
            try:
                if driver.find_element(By.XPATH,'//*[@id="__mbox-btn-0-BDI-content"]'):
                    cerrar=driver.find_element(By.XPATH,'//*[@id="__mbox-btn-0-BDI-content"]')#//*[@id="__mbox-btn-1-BDI-content"]
                elif driver.find_element(By.XPATH,'//*[@id="__mbox-btn-1-BDI-content"]'):
                    cerrar=driver.find_element(By.XPATH,'//*[@id="__mbox-btn-1-BDI-content"]')
                time.sleep(1)
                cerrar.click()
                continue
            except:
                break
        except:
            print("no asignado ")
####################################################################################################################################################3
#######################################################################  FORMATO DE FECHA    ############################################################
def formatof(fecha):
    fechad = fecha.split("/")
    fechan = "".join(fechad)
    formato=fechan.split(" ")
    lafecha=formato[0]
    fechas=lafecha.split("-")
    fecha_n="".join(fechas)
    return fecha_n
###
def calcular_fechas():
    # Obtener la fecha actual
    fecha_actual = datetime.now().date()

    # Calcular la fecha de dos meses en adelante
    fecha_futura = fecha_actual + relativedelta(months=2)

    return  fecha_futura

# Llamar a la función y obtener las fechas
fecha_futura = calcular_fechas()
    


##################################################INGRESAR#############################
def iniciar_sesion():
    while True:
        try:
            driver.get("https://performancemanager8.successfactors.com/login?bplte_logout=1&company=comunicaci&_s.crb=VG1RqGoWUmkzkcagqGY%252fybzahzatv77ql1k8j0nbZ2E%253d#/login")

            driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys("EC7061B")
            driver.find_element(By.XPATH,'//*[@id="__input2-inner"]').send_keys("Onecont2025*")
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
    ex=str(row[1])
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
    fecha_ex=formatof(ex)
    sexo="FEMENINO"
    estadoc="CASADO"
    time.sleep(2)

    fecha_ft=fecha_futura.strftime('%d%m%Y')
    #//*[@id="main--globalSFHeader"]
    texto="Añadir trabajador temporal"
    temporal(texto)
    #ssff()
    time.sleep(1)
    try:
        fechanaci=datetime.strptime(fechan,"%Y%m%d")
        fx= datetime.strptime(fecha_ex, "%Y%m%d")
    except ValueError:
        continue

        # Formatea la fecha en el nuevo formato (DDMMYYYY)
    fecha_expedicion = fx.strftime("%d%m%Y")
    fecha_naci=fechanaci.strftime("%d%m%Y")
    #driver.get("https://performancemanager8.successfactors.com/sf/home?bplte_company=comunicaci&_s.crb=2TUciEoM%2b9O44AcjHb01h2aVK7SLjpZl13QK2%2foTuqs%3d")
    estado=ingresar(nombre, apellido, fecha_naci,pais,cedula,fecha_expedicion)
    #time.sleep(20)
    n=0

    print(estado)

        
    time.sleep(2)
    if estado == "sesado":
        ingresar2(nombre, apellido, fechan,pais,cedula,fecha_expedicion,'si' )
        time.sleep(5)
    elif estado=="añadir":
        print(correo)
        correo_telefono(correo_corporativo,semilla,celular,correo)
        time.sleep(2)
        asignacion(nombre,apellido,fecha_ft,campaña)
        time.sleep(20)
        temporal_intro("inicio")
        #time.sleep(20)
        #otro temporal
        #//*[@id="__link5"]
        #centro de administracion
        #//*[@id="__link0"]

    elif estado=="activo":
        notification = Notify()
        notification.title = "persona activa con aliado"
        notification.message = "captura guardada en carpeta capturas."
        notification.send()
        driver.find_element(By.XPATH,'//*[@id="__button25-BDI-content"]').click()
        time.sleep(1)
        #//*[@id="__mbox-btn-0-BDI-content"]
        driver.find_element(By.XPATH,'//*[@id="__mbox-btn-0-BDI-content"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="__button5-BDI-content"]').click()
        time.sleep(1)
        driver.get("https://performancemanager8.successfactors.com/sf/home?bplte_company=comunicaci&_s.crb=2TUciEoM%2b9O44AcjHb01h2aVK7SLjpZl13QK2%2foTuqs%3d")
        continue
        


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

        