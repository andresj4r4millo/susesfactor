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

driver= webdriver.Edge(executable_path='msedgedriver.exe')
workbook = openpyxl.load_workbook('SSFF.xlsx', read_only=True, data_only=True, keep_links=False, keep_vba=False)
# Seleccionar la hoja de cálculo que deseas leer
sheet = workbook['Hoja1']
def parte1(nombre,apellido,fecha_n,pais):
    while True:
        try:
            buscador=driver.find_element(By.XPATH,'//*[@id="ui5wc_14-inner"]')
            buscador.send_keys("Añadir trabajador temporal")
            buscador.send_keys(Keys.ENTER)
            time.sleep(2)
            #EMPRESA
            #ONE CONTACT INTERNACIONAL (CA661)
            driver.find_element(By.XPATH,'//*[@id="__box0-inner"]').send_keys("ONE CONTACT INTERNACIONAL (CA661)")
            #//*[@id="__item26-__box0-popup-list-0-content"]/div/div
            driver.find_element(By.XPATH,'//*[@id="__item26-__box0-popup-list-0-content"]/div/div').click()
            #PREINGRESO
            driver.find_element(By.XPATH,'//*[@id="__box1-arrow"]').click()
            driver.find_element(By.XPATH,'//*[@id="__item30-__box1-popup-list-0-content"]/div/div').click()
            #NOMBRE
            driver.find_element(By.XPATH,'//*[@id="__input0-inner"]').send_keys(nombre)
            #APELLIDO
            driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys(apellido)
            #FECHA NACIMIENTO
            driver.find_element(By.XPATH,'//*[@id="__picker1-inner"]').send_keys(fecha_n)
            
            if pais !="COLOMBIA":
                driver.find_element(By.XPATH,'//*[@id="__box2-arrow"]').click()
                #PAIS
                driver.find_element(By.XPATH,'//*[@id="__box2-inner"]').send_keys(pais)
                time.sleep(1)
                driver.find_element(By.XPATH,'//*[@id="__item249-content"]/div/div').click()
                #DEPARTAMENTO
                driver.find_element(By.XPATH,'//*[@id="__box3-inner"]').send_keys("Otros departamentos")
                time.sleep(1)
                driver.find_element(By.XPATH,'//*[@id="__item6-__box3-popup-list-0-content"]/div/div').click()

                #CIUDAD
                driver.find_element(By.XPATH,'//*[@id="__box4-arrow"]').click()
                driver.find_element(By.XPATH,'//*[@id="__box4-inner"]').send_keys("otros")
                time.sleep(1)
                driver.find_element(By.XPATH,'//*[@id="__item11-__box4-popup-list-1-content"]/div/div').click()
                
            else:
                driver.find_element(By.XPATH,'//*[@id="__box2-arrow"]').click()
                #PAIS
                driver.find_element(By.XPATH,'//*[@id="__box2-inner"]').send_keys(pais)
                time.sleep(1)
                driver.find_element(By.XPATH,'//*[@id="__item51-content"]/div/div').click()
                #DEPARTAMENTO
                driver.find_element(By.XPATH,'//*[@id="__box3-inner"]').send_keys("Antioquia")
                time.Sleep(1)
                driver.find_element(By.XPATH,'//*[@id="__item7-__box3-popup-list-0-content"]/div/div').click()
            #NOMBRE USUARIO
            
            


            break
        except:
            continue


driver.get("https://performancemanager8.successfactors.com/login?bplte_logout=1&company=comunicaci&_s.crb=VG1RqGoWUmkzkcagqGY%252fybzahzatv77ql1k8j0nbZ2E%253d#/login")
# Iterar sobre las filas en la hoja de cálculo
time.sleep(1)
#paso=input()
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys("EC7061B")
        driver.find_element(By.XPATH,'//*[@id="__input2-inner"]').send_keys("Onecont2024*")
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="__button2-content"]').click()
        time.sleep(4)
        break
    except:
        print("a")
while True:
    try:
        time.sleep(3)
        cabecera=driver.find_element(By.XPATH,'//*[@id="container"]/div[1]')
        print("encontrada")
        break
        #//*[@id="shellbar"]//header/div[3]/div/div
        #//*[@id="ui5wc_19-inner"]
    except:
        print("a")
