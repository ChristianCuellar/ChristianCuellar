
# Versión que imprime por consola el método de eratóstenes.

numero_tope = int(input("Ingrese un numero: "))
casillas = {}

# Se construye un diccionario con el universo de números disponibles
for casilla in range(2, numero_tope + 1):
    casillas[casilla] = str(casilla)


def buscarMultiplos(numero_base):
    multiplos = []
    for numero in range(numero_base + 1, numero_tope + 1):
        if(numero % numero_base == 0):
            multiplos.append(numero)
    return multiplos

def mostrarResultado():
    salida = []
    #casillas[3] = "aasd"
    for casilla in casillas:
        if(casillas[casilla].isdigit()):
            salida.append(str(casilla))
        else:
            salida.append("X")
    print(" - ".join(salida))

"""
Pasos desde https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes

1.- Listar los números naturales comprendidos entre 2 hasta el número que se desee.
2.- Se toma el primer número no marcado como número primo.
3.- Se marcan todos los múltiplos del número que se acaba de indicar como primo.
4.- Si el cuadrado del primer número que no ha sido marcado es inferior al numero_tope,
    entonces se repite el segundo paso. Si no, el algoritmo termina, y todos los
    enteros no tachados son declarados primos.
"""
mostrarResultado()

for valor in casillas:
    if(casillas[valor] == "X"):
        continue

    for numero in buscarMultiplos(valor):
        casillas[numero] = "X"
    mostrarResultado()
    if(valor ** 2 > numero_tope):
        break
