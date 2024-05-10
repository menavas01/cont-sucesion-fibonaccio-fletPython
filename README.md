#Contador Sucesion De Fibonacci

Logica del programa:

1- Usar un arreglo (inicio) para guardar los numeros generados de la sucesion de Fibonacci
2- Usar un contador (cont) para saber en que parte de la sucesion estamos

El arreglo se inicializa con: inicio = [0, 1]. Esto para tener los primeros dos valores para sumar a la sucesion.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Se crea una fucion para sumar, esta agrega los siguientes numeros de la sucesion, sumando el ultimo número del arreglo y el anterior. Como arranca en 0 el contador,
se crea el siguiente número de la sucesion asi: inicio.append.(inicio[cont] + inicio[cont+1]). 
Una vez generado un nuevo número de la sucesion sumamos 1 al contador (cont += 1).

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Se crea una fucion para restar, esta elimina el último número del arrego así: inicio.pop(). Esto lo hacemos para evitar conflictos, ya que de no hacerlo podemos generar
nuevamente la sucesion en un lugar del arreglo donde no corresponde, haciendo que no funcione correctamente la aplicacion. Una vez eliminado el número de la sucesion 
restamos 1 al contador (cont -= 1).

Ejemplo de lo que pasa si NO eliminamos el último elemento del arreglo:

Todo funciona correctamente en sumar, genera el arreglo correctamente y el contador funciona:
inicio = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
cont = 9

Ahora si restamos lo que sucedera es que el contador decrementa, pero el arreglo se mantiene:
inicio = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
cont = 0

Si intentamos generar nuevos números en la sucesion lo que hara el programa es lo siguiente:
inicio = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 2, 3, 5] 
cont = 4

Esto genera nuevamente a la sucesion lo que hara que una vez llegue al punto donde se genero nuevamente la sucesion, repita números anteriores:
inicio = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 2, 3, 5 ..... ] 
cont = 11
(Aquí el programa volveria a mostrar el número 1, ya que lo que hace es mostrar lo que hay en el arreglo en la posicion 11: inicio[11])

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

El contador es usado para saber en que punto de la secuencia estamos, usandose como indice en el arreglo: inicio [cont]