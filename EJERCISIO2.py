import random

# Generar un número aleatorio entre 0 y 359 grados para la posición inicial
posicion_inicial = random.randint(0, 359)

# Generar un número aleatorio entre 5 y 10 para las vueltas al círculo
vueltas = random.randint(5, 10)

# Calcular el ángulo final
angulo_final = (posicion_inicial + vueltas * 360) % 360

# Imprimir los resultados
print(f"Posición o ángulo Inicial G.A.: {posicion_inicial}")
print(f"Valor Aleatorio Generado en Grados: {vueltas * 360}")
print(f"Ángulo Final: {angulo_final}")
