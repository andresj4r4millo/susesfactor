import re
import datetime
import pymysql


# Texto de ejemplo
texto = "324 2078956 Lorena ajdjvdgaks jsjdhsjjad Jsjsjsjs jdjdjdjjd zkdijdhdud 35753888 13 min"

# Busca los primeros 10 números en el texto
patron = r'\d{10}'
txt = re.sub(r'[^0-9]', '', texto)

primeros_10 = txt[:10]

# Corta los siguientes 6 dígitos y almacénalos en otra variable
codigo = txt[10:16]
campaña="hogar"

# Imprime las variables resultantes
print("Primeros 10 dígitos:", primeros_10)
print("Siguientes 6 dígitos:", codigo)
hora_actual = datetime.datetime.now()
hora = hora_actual.strftime('%H:%M')

# Imprime la hora formateada
print(hora)
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

    print("Sentencia SQL ejecutada con éxito")
except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar el cursor y la conexión
    if cursor:
        cursor.close()
    if conn:
        conn.close()

