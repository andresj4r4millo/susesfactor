#from notifypy import Notify
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from notifypy import Notify
import re
import datetime
import pymysql

driver= webdriver.Edge()
driver.maximize_window()


tokens={}
# Abrir una página web en el navegador
driver.get("https://messages.google.com/web/conversations/20")
while True:
    print("MENU DE OPCIONES: ")

    print("digite 1 para hogar ")
    print("digite 2 para movil ")
    print("digite 3 para portabilidad ")
    print("digite 4 para migracion ")
    print("digite 5 para grupo elite ")
    print("digite 6 para comunidad ")
    print("digite 7 para uraba ")
    print("digite 8 para backoffice ")
    opc=input("digite opcion de campaña: ")
    if opc==1 or opc=='1':
        campaña="hogar"
        break
    elif opc==2 or opc=='2':
        campaña="movil"
        break
    elif opc==3 or opc=='3':
        campaña="portabilidad"
        break
    elif opc==4 or opc=='4':
        campaña="migracion"
        break
    elif opc==5 or opc=='5':
        campaña="elite"
        break
    elif opc==6 or opc=='6':
        campaña="comunidad"
        break
    elif opc==7 or opc=='7':
        campaña="uraba"
        break
    elif opc==8 or opc=="8":
        campaña="back"
        break
    else:
        print("opcion no valida, vuelva a digitar ")
        continue

while True:

    opc=input("estas dentro?: ")
    if opc=="si" or opc=="SI" or opc=="Sí":
        opc="si"
        break
    else:
        continue
if opc=="si":
    while True:
        try:
            reciente=driver.find_element(By.XPATH,'/html/body/mw-app/mw-bootstrap/div/main/mw-main-container/div/mw-main-nav/mws-conversations-list/nav/div[1]/mws-conversation-list-item[1]')
            reciente.click()

            cadena=reciente.text
            expresion_regular =  r'\((\d+)\)'
            texto=re.sub(expresion_regular, '', cadena)


            txt = re.sub(r'[^0-9]', '', texto)

            remitente = txt[:4]

            # Corta los siguientes 6 dígitos y almacénalos en otra variable
            codigo = txt[4:12]
            if remitente=="6231":
                if codigo not in tokens:
                    hora_actual = datetime.datetime.now()
                    la_hora=hora_actual.strftime('%H:%M')
                    tokens[codigo]=la_hora
                    hora=tokens[codigo]
                    ############
                    try:
                        conn = pymysql.connect(
                            host="10.206.69.198",
                            port=12125,
                            user="mysqldb",
                            password="Colombia2025=",
                            database="token"
                        )
                        cursor = conn.cursor()

                        # Sentencia SQL de inserción
                        sql = "INSERT INTO tokens (campaña, codigo, hora) VALUES (%s, %s, %s)"

                        # Valores a insertar
                        valores = (campaña, codigo, hora)

                        # Ejecutar la sentencia SQL
                        cursor.execute(sql, valores)

                        # Confirmar la transacción
                        conn.commit()

                        print("mensaje recibido")
                    except Exception as e:
                        print(f"Error: {e}")

                    finally:
                        # Cerrar el cursor y la conexión
                        if cursor:
                            cursor.close()
                        if conn:
                            conn.close()

                    ############

        except Exception as e:
            print(f"no se pudo interactuar error: {e}")
        # Imprime el texto
    

