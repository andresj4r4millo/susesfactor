from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcular_fechas():
    # Obtener la fecha actual
    fecha_actual = datetime.now().date()

    # Calcular la fecha de dos meses en adelante
    fecha_futura = fecha_actual + relativedelta(months=2)

    return fecha_actual, fecha_futura

# Llamar a la función y obtener las fechas
fecha_actual, fecha_futura = calcular_fechas()

print("Fecha actual:", fecha_actual.strftime('%Y%m%d'))
print("Fecha de dos meses en adelante:", fecha_futura.strftime('%Y%m%d'))
