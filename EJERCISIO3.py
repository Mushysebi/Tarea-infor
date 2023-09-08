import random
from datetime import datetime, timedelta

# Obtener la hora actual
hora_actual = datetime.now()

# Generar un número aleatorio de minutos entre 300 (5 horas) y 600 (10 horas)
minutos_aleatorios = random.randint(300, 600)

# Calcular la hora final sumando los minutos aleatorios a la hora actual
hora_final = hora_actual + timedelta(minutes=minutos_aleatorios)

# Imprimir los resultados formateados
print("Hora Actual:", hora_actual.strftime("%H:%M"))
print("Valor Aleatorio Generado en Minutos:", minutos_aleatorios)
print("Hora Final:", hora_final.strftime("%H:%M"))
