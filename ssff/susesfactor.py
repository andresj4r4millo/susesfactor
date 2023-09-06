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
from selenium.webdriver.edge.service import Service as EdgeService
import os
from datetime import datetime
#import funciones

edge_service = EdgeService('msedgedriver.exe')

# Inicializa el controlador de Edge
driver = webdriver.Edge(service=edge_service)
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
            try:
                buscador = segundo_shadow_root.find_element(By.ID, "ui5wc_14-inner")#//*[@id="ui5wc_8-inner"]
            except:
                buscador=segundo_shadow_root.find_element(By.ID,"ui5wc_19-inner")
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
            try:
                primer_etiqueta=driver.find_element(By.XPATH, '//*[@id="renderTopNavSFHeader"]/xweb-shellbar')
            except:
                primer_etiqueta=driver.find_element(By.XPATH, '//*[@id="bizXShellBarContainer"]/xweb-shellbar')
                #//*[@id="bizXShellBarContainer"]/xweb-shellbar
            primer_shadow_root = driver.execute_script('return arguments[0].shadowRoot', primer_etiqueta)
            segunda_etiqueta = primer_shadow_root.find_element(By.ID,"search")
            segundo_shadow_root = driver.execute_script('return arguments[0].shadowRoot', segunda_etiqueta)
            try:
                buscador = segundo_shadow_root.find_element(By.ID, "ui5wc_8-inner")#//*[@id="ui5wc_8-inner"]
            except:
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
            fx.clear()
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
                driver.find_element(By.XPATH,'//*[@id="__mbox-btn-0-inner"]').click()
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
                    time.sleep(8)
                    return "activo"
                elif "cesado" in ventana_e.text.lower():

                    try:
                        #seleccion generica
                        driver.find_element(By.XPATH,'//*[@id="__photo0-UserSearchResult--newHireUserMatchList-1-inner"]/div/img').click()
                        time.sleep(1)
                        driver.find_element(By.XPATH,'//*[@id="__button23-BDI-content"]').click()
                        # si
                        driver.find_element(By.XPATH,'//*[@id="__mbox-btn-1-inner"]').click()
                        time.sleep(2)
                        return "cesado"

                    except Exception as e:
                        print(e)
                    print("cesado")

            except:
                return "añadir"
            

        except:
            print("datos erroneos")
            
def fun_activo():
    while True:
        try:
            print(1)
            #time.sleep(20)
            if "El nombre del usuario ya existe. Introduzca un nuevo valor exclusivo." in driver.page_source:
                #cerrar 
                driver.find_element(By.XPATH,'//*[@id="__mbox-btn-0-BDI-content"]').click()
            #guardar borrador
            driver.find_element(By.XPATH,'//*[@id="__link0"]').click()  
            if "Hay datos sin guardar en la página. ¿Seguro que desea salir sin guardarlos?"  in driver.page_source:
                driver.find_element(By.XPATH,'//*[@id="__button26-BDI-content"]').click()
                break

            #El nombre del usuario ya existe. Introduzca un nuevo valor exclusivo.
            #//*[@id="__mbox-btn-1-BDI-content"]
            
        except:
            print("2")



##################################################################################################
def cesado(nombre, apellido, fecha_naci,pais,cedula,fecha_expedicion,codigo_p ):
   
    while True:
        try:

            elemento_input = driver.find_element(By.ID,"__box10-inner")
            #//*[@id="__box10-inner"]
            texto="ONE CONTACT INTERNACIONAL (CA661)"
            driver.find_element(By.XPATH,'//*[@id="__box10-arrow"]').click()
            elemento_input.send_keys("661")
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box10-popup-cont"]//div[text()="{texto}"]')))
            #//*[@id="__box0-popup-list-listUl"]
            opcion.click()
            time.sleep(1)
            #motivo
            driver.find_element(By.XPATH,'//*[@id="__box11-arrow"]').click()

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
            opcion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box11-popup-cont"]//div[text()="{opciont}"]')))
            opcion.click()
            time.sleep(1)
            cd_p=driver.find_element(By.XPATH,'//*[@id="__input20-inner"]')
            cd_p.clear()
            cdp=f"{cedula}CA661"
            cd_p.send_keys(cdp)

            #### continuar
            driver.find_element(By.XPATH,'//*[@id="__button38-BDI-content"]').click()
            time.sleep(2)
            crr=driver.find_element(By.XPATH,'//*[@id="__input28-inner"]')
            crr.click()
            if "Motivo del evento es obligatorio" in driver.page_source:
                driver.find_element(By.XPATH,'//*[@id="__mbox-btn-2-BDI-content"]').click()
                continue
            break
        except:
            print("error3")
    #continuar


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
def correo_tel_2(correo_corporativo,semilla,celular,correo):
    #correo
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__box19-arrow"]').click()
            tc="Corporativo"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box19-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            correoc=driver.find_element(By.XPATH,'//*[@id="__input28-inner"]')
            actions.double_click(correoc).perform()
            correoc.send_keys(correo)
            driver.find_element(By.XPATH,'//*[@id="__box20-arrow"]').click()
            tc="Sí"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box20-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            #añadir o añadido
            driver.find_element(By.XPATH,'//*[@id="__box21-arrow"]').click()
            #
            tc="Personal"
            opcionp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box21-popup-cont"]//div[text()="{tc}"]')))
            opcionp.click()
            #
            cp=driver.find_element(By.XPATH,'//*[@id="__input31-inner"]')
            cp.clear()
            cp.send_keys(correo_corporativo)
            #
            tc="No"
            driver.find_element(By.XPATH,'//*[@id="__box22-arrow"]').click()
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box22-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            #############################################
            break
        except:
            print(correo)

    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__box23-arrow"]').click()
            #//*[@id="__box21-popup-cont"]
            tc="Corporativo"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box23-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            #
            nm=driver.find_element(By.XPATH,'//*[@id="__input34-inner"]')
            nm.clear()
            nm.send_keys(semilla)
            time.sleep(1)
            print("primer")
            pr=driver.find_element(By.XPATH,'//*[@id="__box24-inner"]')
            pr.clear()
            pr.send_keys("Sí")
            tc="Sí"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box24-popup-cont"]//div[text()="{tc}"]')))
            opcionx.click()
            # añadir o añadido
            print("primer cel")
            try:
                print("entra")
                driver.find_element(By.XPATH,'//*[@id="__box25-arrow"]').click()
                tc="Personal"
                opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box25-popup-cont"]//div[text()="{tc}"]')))
                opcionx.click()
                correoc=driver.find_element(By.XPATH,'//*[@id="__input37-inner"]')
                actions.double_click(celular).perform()
                correoc.send_keys(correo_corporativo)
                driver.find_element(By.XPATH,'//*[@id="__box26-arrow"]').click()
                tc="No"
                opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box26-popup-cont"]//div[text()="{tc}"]')))
                opcionx.click()
            except:
                #añadir 
                driver.find_element(By.XPATH,'//*[@id="__button57-content"]').click()

                driver.find_element(By.XPATH,'//*[@id="__box25-arrow"]').click()#//*[@id="__box25-arrow"]
                tc="Personal"
                opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box25-popup-cont"]//div[text()="{tc}"]')))
                opcionx.click()
                correoc=driver.find_element(By.XPATH,'//*[@id="__input37-inner"]')
                actions.double_click(correoc).perform()
                correoc.send_keys(semilla)
                driver.find_element(By.XPATH,'//*[@id="__box26-arrow"]').click()
                tc="No"
                opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box26-popup-cont"]//div[text()="{tc}"]')))
                opcionx.click()

            
            #continuar
            driver.find_element(By.XPATH,'//*[@id="__button52-BDI-content"]').click()

            #otrapagina
            driver.find_element(By.XPATH,'//*[@id="__box29-inner"]').click()
            break
        except:
            print(semilla)

##############################################################################
##################################################################################

def asignacion_cesado(nombre,apellido,fecha_ft,campaña):
    while True:
        try:
            #posicion
            
            driver.find_element(By.XPATH,'//*[@id="__box29-arrow"]').click()
            pt=driver.find_element(By.XPATH,'//*[@id="__box29-inner"]')
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
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box29-popup-cont"]//div[text()="{puesto}"]')))
            opcionx.click()
            #direccion
            #driver.find_element(By.XPATH,'//*[@id="__box23-arrow"]').click()
            time.sleep(3)
            #ubicacion
            driver.find_element(By.XPATH,'//*[@id="__box33-arrow"]').click()
            ubicacion="SEDE ALIADO (6100210)"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box33-popup-cont"]//div[text()="{ubicacion}"]')))
            opcionx.click()
            print("ya casi")

            driver.find_element(By.XPATH,'//*[@id="__button74-BDI-content"]').click()
            break
        except:
            print("error de asignacion  ")
    time.sleep(10)
    ### work order
    while True:
        try:
            # fecha fin 2 meses
            FF=driver.find_element(By.XPATH,'//*[@id="__picker10-inner"]')#//*[@id="__picker7-inner"]

            FF.send_keys(fecha_ft)
            nombrec=(f"{nombre} {apellido}")
            cd=driver.find_element(By.XPATH,'//*[@id="__input61-inner"]')
            cd.clear()
            cd.send_keys(cedula)
            #
            nom=driver.find_element(By.XPATH,'//*[@id="__input62-inner"]')#
            nom.clear()
            nom.send_keys(nombrec)

            #GESTOR INFORMACION ALIADO ONE CONTACT INTERNACIONAL
            dueño=driver.find_element(By.XPATH,'//*[@id="__box43-inner"]')
            dueño.clear()
            dueño.send_keys("GESTOR")#
            dueno="GESTOR INFORMACION ALIADO ONE CONTACT INTERNACIONAL"
            time.sleep(2)
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box43-popup-cont"]//div[text()="{dueno}"]')))
            opcionx.click()

            #proveedor
            driver.find_element(By.XPATH,'//*[@id="__box44-arrow"]').click()
            #CA661
            prov=driver.find_element(By.XPATH,'//*[@id="__box44-inner"]')
            prov.clear()

            prov.send_keys("CA661")
            provedor="CA661 (ONE CONTACT INTERNACIONAL)"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box44-popup-cont"]//div[text()="{provedor}"]')))
            opcionx.click()
            
            #fechaf.clear()
            print("asignado")
            #continuar
            time.sleep(2)
            driver.find_element(By.XPATH,'//*[@id="__button81-BDI-content"]').click()
            
            try:
                if driver.find_element(By.XPATH,'//*[@id="__mbox-btn-2-BDI-content"]'):
                    cerrar=driver.find_element(By.XPATH,'//*[@id="__mbox-btn-2-BDI-content"]')#//*[@id="__mbox-btn-1-BDI-content"]
                elif driver.find_element(By.XPATH,'//*[@id="__mbox-btn-1-BDI-content"]'):
                    cerrar=driver.find_element(By.XPATH,'//*[@id="__mbox-btn-1-BDI-content"]')
                time.sleep(1)
                carpeta_añadidos="añadidos"
                if not os.path.exists(carpeta_añadidos):
                    os.makedirs(carpeta_añadidos)
                    print("preparando navegador para captura")

                    screenshot_name = f'capturas/{cedula}CA661.png'
                    driver.save_screenshot(screenshot_name)
                cerrar.click()
                continue
            except:
                time.sleep(1)
                driver.find_element(By.XPATH,'//*[@id="__link0"]')
                break
        except:
            print("no asignado ")
    return True

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
                carpeta_añadidos="añadidos"
                if not os.path.exists(carpeta_añadidos):
                    os.makedirs(carpeta_añadidos)
                    print("preparando navegador para captura")

                    screenshot_name = f'capturas/{cedula}CA661.png'
                    driver.save_screenshot(screenshot_name) 

                cerrar.click()
                continue
            except:
                break
        except:
            print("no asignado ")
    return True
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
trabajadores=[]
activos=[]
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
    if cedula=="None":
        break
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
    trabajador_temporal=False
    
    time.sleep(2)
    if estado == "cesado":
        cesado(nombre, apellido, fechan,pais,cedula,fecha_expedicion,'si' )
        time.sleep(1)
        correo_tel_2(correo_corporativo,semilla,celular,correo)
        time.sleep(1)
        trabajador_temporal=asignacion_cesado(nombre,apellido,fecha_ft,campaña)
        temporal_intro("inicio")
        

    elif estado=="añadir":
        print(correo)
        correo_telefono(correo_corporativo,semilla,celular,correo)
        time.sleep(2)
        trabajador_temporal=asignacion(nombre,apellido,fecha_ft,campaña)
        time.sleep(20)
        temporal_intro("inicio")

    elif estado=="activo":
        print("el estado")
        #ignorar
        driver.find_element(By.XPATH,'//*[@id="__button25-BDI-content"]').click()
        fun_activo()
        time.sleep(1)
        activos.append(cedula)
        temporal_intro("inicio")
        #driver.get("https://performancemanager8.successfactors.com/sf/home?bplte_company=comunicaci&_s.crb=2TUciEoM%2b9O44AcjHb01h2aVK7SLjpZl13QK2%2foTuqs%3d")
        continue
    
    if trabajador_temporal== True:
        usuario=f"{cedula}-{nombre} {apellido}"
        trabajadores.append(usuario)

if len(trabajadores) > 0:    
    with open('trabajadores_temporales.txt', 'w') as archivo:
        for trabajador in trabajadores:
            archivo.write(trabajador + '\n')
if len(activos) > 0:
    with open('trabajadores_activos.txt', 'w') as archivo:
        for trabajador in activos:
            archivo.write(trabajador + '\n')
    



print("terminao")




############################################################################################
################INGRESO

        