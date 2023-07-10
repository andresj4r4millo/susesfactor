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
def parte1(nombre,apellido,fecha_n):
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
            print("diligenciados")#//*[@id="__picker3-inner"]
            time.Sleep(4)
        
            break
        except:
            print("nod")
            continue

def agregar():
    time.sleep(1)
    #paso=input()
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
        ##1
    while True:
        try:
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/section/ul/li[5]/ui5-busy-indicator/a').click()
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="__xmlview0--newHireButton-img"]').click()
            time.sleep(3)
            elemento_input = driver.find_element(By.XPATH, '//*[@id="__box0-inner"]')
            elemento_input.click()
            elemento_input.send_keys("661")
            time.sleep(2)
            elemento_input.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            elemento_input.send_keys(Keys.ENTER)
            time.sleep(1)#
            break
        except:
            print("Error al buscar e interactuar con elementos")
            continue

        ##2
    while True:
        try:
            coso=driver.find_element(By.XPATH, '//*[@id="__box1-inner"]')
            
            coso.send_keys("Nueva")
            time.sleep(1)
            coso.send_keys(Keys.ARROW_DOWN)
            coso.send_keys(Keys.ARROW_DOWN)
            coso.send_keys(Keys.ARROW_DOWN)
            coso.send_keys(Keys.ENTER)
            print("KJHJGHGH")
            print("Encontrado")
            break
        except:
            print("Error al buscar e interactuar con elementos")
            continue

    ##3
    while True:
        try:
            #desplegar=driver.find_element(By.XPATH, '//*[@id="__box1-inner"]')
            desplegar=driver.find_element(By.XPATH, '//*[@id="__box2-inner"]')
            desplegar.send_keys("Contratación Claro")
            time.sleep(3)
            desplegar.send_keys(Keys.ARROW_DOWN)
            desplegar.send_keys(Keys.ENTER)
        
            
            time.sleep(5)
            break
        except:
            print("Error al buscar e interactuar con elementos")
    driver.find_element(By.XPATH,'//*[@id="__button1-content"]').click()

driver.get("https://performancemanager8.successfactors.com/login?bplte_logout=1&company=comunicaci&_s.crb=VG1RqGoWUmkzkcagqGY%252fybzahzatv77ql1k8j0nbZ2E%253d#/login")
# Iterar sobre las filas en la hoja de cálculo

agregar()
time.sleep(4)
nombre="juan"
apellido="alvarez"
fecha_n="02/04/2002"
pais="ecuador"
parte1(nombre,apellido,fecha_n)
time.sleep(6)


