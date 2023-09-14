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

edge_service = EdgeService('msedgedriver.exe')

# Inicializa el controlador de Edge
driver = webdriver.Edge(service=edge_service)
driver.maximize_window()
driver.implicitly_wait(4)
actions = ActionChains(driver)
workbook = openpyxl.load_workbook('SSFF.xlsx', read_only=True, data_only=True, keep_links=False, keep_vba=False)
# Seleccionar la hoja de cálculo que deseas leer
sheet = workbook['Hoja1']
###################
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

            time.sleep(2)
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
            time.sleep(1)
            buscador.send_keys(Keys.ARROW_DOWN)
            buscador.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            buscador.send_keys(Keys.ENTER)

            print("tambien se encontro")

            time.sleep(2)
            break
        except Exception as e:

            print("No se pudo interactuar:", e)
######################
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
def formatof(fecha):
    fechad = fecha.split("/")
    fechan = "".join(fechad)
    formato=fechan.split(" ")
    lafecha=formato[0]
    fechas=lafecha.split("-")
    fecha_n="".join(fechas)
    return fecha_n
###################### PRE INGRESO##############
def preingreso():
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__xmlview0--objectPage-anchBar-__section1-__xmlview0--objectPage-5-anchor-internalSplitBtn-textButton-BDI-content"]').click()
            break
        except:
            print("no se pudo interactuar")
    while True:
        try:
            #//*[@id="__button71-inner"]
            prei=driver.find_element(By.XPATH,'//*[@id="__xmlview0--objectPage-anchBar-__section1-__xmlview0--objectPage-7-anchor-content"]')
            prei.click()
            try:
                cust=driver.find_element(By.XPATH,'//*[@id="__button65-inner"]')
            except:
                cust=driver.find_element(By.XPATH,'//*[@id="__button71-inner"]')
            cust.click()
            break
        except Exception as e:

            print(f"error pre ingreso: {e}")
    while True:
        try:
            fm=driver.find_element(By.XPATH,'//*[@id="__box4-arrow"]')
            fm.click()
            tf="No (No)"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box4-popup-cont"]//div[text()="{tf}"]')))
            opcionx.click()

            fam=driver.find_element(By.XPATH,'//*[@id="__box5-arrow"]')
            fam.click()
            familiares=driver.find_element(By.XPATH,'//*[@id="__box5-inner"]')
            familiares.clear()
            familiares.send_keys("no")
            tf="No Aplica (07)"
            opcionx = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__box5-popup-cont"]//div[text()="{tf}"]')))
            opcionx.click()
            time.sleep(1)
            print("continuar")
            #continuar
            try:
                driver.find_element(By.XPATH,'//*[@id="__button76-content"]').click()
            except:
                driver.find_element(By.XPATH,'//*[@id="__button80-content"]').click()
            #//*[@id="__button80-content"]
            #//*[@id="__button80-inner"]
            #//*[@id="__button80"]
            ## //*[@id="__button76-inner"]
            #//*[@id="__button76-content"]
            break

        except Exception as e:
            print(f"err familiares: {e}")

iniciar_sesion()

temporal("JOSE HANDERS GAMBOA ECHEVERRY")
time.sleep(20)
preingreso()
time.sleep(20)

    
