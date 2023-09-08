import random

def simular_tirada():
    # Generar un número aleatorio entre 5 y 10 vueltas
    vueltas = random.randint(5, 10)
    
    # Generar un número aleatorio entre 0 y 36 para representar la posición inicial
    posicion_inicial = random.randint(0, 36)
    
    # Calcular la posición final
    posicion_final = (posicion_inicial + vueltas) % 37
    
    return vueltas, posicion_final

# Simular 10 tiradas e imprimir los resultados
for juego in range(1, 11):
    vueltas, posicion_final = simular_tirada()
    print(f"Nro de Juego: {juego}")
    print(f"Valor Aleatorio Generado: {vueltas}")
    print(f"Nro que cayó en la ruleta: {posicion_final}")
    print()
