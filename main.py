# Importamos la librería Flet
import flet as ft

# Definimos la función principal
def main(page: ft.Page):

    # Contador para iterar
    cont = 0

    # Inicio de la sucesión de Fibonacci
    inicio = [0, 1]

    # Título de la página
    page.title = "Contador sucesión de Fibonacci"

    # Alineación vertical de la página
    page.vertical_alignment = "center"

    # Texto para el título
    nombre = ft.Text(
        value= (f"Número {cont} de sucesión de Fibonacci")
    )

    # Caja de texto para el número a contar
    txt_number = ft.TextField(
        value="0",
        text_align="center",
        width=100,
        read_only=True
    )

    # Función para sumar en la sucesión de Fibonacci
    def fibonacci_suma():
        # Usamos esta declaracion para que la funcion pueda acceder a las variables cont e inicio
        nonlocal cont, inicio

        # Agregamos el siguiente valor a la lista (suma del número actual + el anterior)
        inicio.append(inicio[cont] + inicio[cont + 1])
        print(inicio, cont)
        
        # Sumamos en uno al contador
        cont += 1

        
    # Función para restar en la sucesión de Fibonacci
    def fibonacci_resta():
        # Usamos esta declaracion para que la funcion pueda acceder a las variables cont e inicio
        nonlocal cont, inicio
        
        # Si el contador no es 1 o 0, eliminamos el último elemento de la lista (Esto para evitar eliminar los valores iniciales inicio = [0, 1])
        if cont!= 1 or cont!= 0:
            inicio.pop()
        print(inicio, cont)
        
        # Restamos en uno al contador
        cont -= 1


    # Función para hacer click en el botón menos
    def minus_click(e):
        # Si el valor del texto es 0, establece el valor del texto en el primer elemento de la lista
        if int(txt_number.value) == 0:
            txt_number.value = inicio[0]
        # Si no, llama a la función de resta
        else:
            fibonacci_resta()
            # Establece el valor del texto en el valor del contador
            txt_number.value = inicio[cont]

        # Actualizamos el valor de nombre para saber en que número de la sucesion estamos
        nombre.value = (f"Número {cont} de sucesión de Fibonacci")
        
        # Actualiza la página
        page.update()

    # Función para hacer click en el botón más
    def plus_click(e):
        # Llama a la función de suma
        fibonacci_suma()
        # Establece el valor del texto en el valor del contador
        txt_number.value = inicio[cont]

        # Actualizamos el valor de nombre para saber en que número de la sucesion estamos
        nombre.value = (f"Número {cont} de sucesión de Fibonacci")
        
        # Actualiza la página
        page.update()

    # Agregamos los elementos a la página
    page.add(
        # Filas con los elementos
        ft.Row(
            [
                nombre
            ],
            alignment="center"
        ),
        ft.Row(
            [
                # Botón menos
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                # Caja de texto con el valor del contador
                txt_number,
                # Botón más
                ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ],
            alignment="center"
        )
    )

# Iniciamos la aplicación con la función principal
ft.app(target=main)