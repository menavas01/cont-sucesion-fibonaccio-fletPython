#Funcionamiento basico del programa
def fibonacci(inicio, cont):
        inicio.append(inicio[cont] + inicio[cont+1])
        cont += 1
        
        return inicio, cont
        
inicio = [0, 1]
cont = 0
siguiente = 1

while True:
        if (siguiente != 0):
                inicio, cont = fibonacci(inicio, cont)
                print(inicio)
                siguiente = input("¡Quieres continuar? 0 para no, cualquier tecla para continuar\n")
        else:
                break

""" Codigo funcional sin gardarlo en un array

def fibonacci(aux, cont, numero):
    if numero == 0:
        print(f"Número {cont} de la sucesión: {numero}")
        siguiente_numero = 1
        cont += 1
        return numero, siguiente_numero, cont

    elif numero == 1 and cont <= 2:
        print(f"Número {cont} de la sucesión: {numero}")
        siguiente_numero = aux + numero
        cont += 1
        return numero, siguiente_numero, cont

    else:
        siguiente_numero = aux + numero
        print(f"Número {cont} de la sucesión: {siguiente_numero}")
        cont += 1
        return numero, siguiente_numero, cont

aux = 0
cont = 1
numero = 0

while True:
    numero, siguiente_numero, cont = fibonacci(aux, cont, numero)
    aux = numero
    numero = siguiente_numero
    continuar = input("\nPresione cualquier tecla para continuar, presione '0' para salir\n")
    if continuar == '0':
        break
        
"""

