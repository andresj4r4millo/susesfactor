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
from datetime import datetime
def formatof(fecha):
    if fecha==None:
        fecha_actual = datetime.now()
        fecha_n = fecha_actual.strftime("%d%m%Y")
        return fecha_n
    fechas = fecha.split("/")
    fechan = "".join(fechas)
    formato=fechan.split(" ")
    lafecha=formato[0]
    fechas=lafecha.split("-")
    fecha_n="".join(fechas)
    return fecha_n

def formatodefecha(fecha):
    if fecha==None:
        fecha_actual = datetime.now()
        fecha_n = fecha_actual.strftime("%d%m%Y")
        return fecha_n
    fechas = fecha.split("/")
    fechan = "".join(fechas)
    formato=fechan.split(" ")
    lafecha=formato[0]
    return lafecha
nuevo_workbook = openpyxl.Workbook()
nueva_sheet = nuevo_workbook.active

workbook = openpyxl.load_workbook('SSFF.xlsx', read_only=True, data_only=True, keep_links=False, keep_vba=False)
# Seleccionar la hoja de cálculo que deseas leer
sheet = workbook['Hoja1']
for index, row in enumerate(sheet.iter_rows(values_only=True), start=1):
    if index==1:
        continue
    cedula=str(row[0])
    fecha_ex=str(row[1])
    fn=str(row[2])
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
    fecha=fn
    print(fecha)
    fch=formatodefecha(fecha)
    print(fch)

    """
    nueva_sheet.cell(row=index, column=1, value=cedula)
    nueva_sheet.cell(row=index, column=2, value=pais)
    
    if fecha == None:
        continue
    else:
        fechan=formatof(fecha)
        expedicion=formatof(fecha_ex)
        # Convierte la fecha a un objeto datetime
        try:
            fecha_objeto = datetime.strptime(fechan, "%Y%m%d")
        except ValueError:
            continue

        # Formatea la fecha en el nuevo formato (DDMMYYYY)
        fecha_formateada = fecha_objeto.strftime("%d%m%Y")

        # Formatea la fecha en el nuevo formato (DD/MM/AAAA)
        fecha_formateada = fecha_objeto.strftime("%d%m%Y")
        print("nacimiento")
        print(fecha)
        print("expedicion")
        #print(fecha_ex)
        print(fecha_formateada)
        print(expedicion)
        #print(fechan)
    """
#nuevo_workbook.save('Nuevo_SSF.xlsx')

    



