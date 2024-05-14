import flet as ft
def main(page: ft.Page):
    def crear_matriz(e):
        n = int(entrada_n.value)
        for i in range(n):
            columna = list()
            for j in range(n):
                # Crea y agrega los campos de texto para las entradas de la matriz
                columna.append(ft.TextField(width=50))
            contenedor.controls.append(ft.Row(columna , alignment="center"))
        page.update()
    
    contenedor = ft.Page()

    page.title = "Matriz nxn"
    page.auto_scroll = True
    entrada_n = ft.TextField(label="Tamaño de la matriz (n):")
    boton_confirmar = ft.ElevatedButton(text="Confirmar", on_click=crear_matriz)
    page.add(entrada_n, boton_confirmar , contenedor)

    

ft.app(main)