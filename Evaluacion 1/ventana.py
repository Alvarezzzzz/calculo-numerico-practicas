import flet as ft
import funciones

#Cedula 31629822 

#Clase del boton personalizado
class MyButton(ft.ElevatedButton):
    def __init__(self, text , on_clicked):
        super().__init__()
        self.bgcolor = ft.colors.DEEP_PURPLE_ACCENT_700 # Color del fondo del boton
        self.color = ft.colors.WHITE #Color de la letra
        self.text = text
        self.on_click = on_clicked
        self.width = 200
        self.height = 50

#Funcion principal que ejecuta la ventana
def main(page: ft.Page):

    #Tab del gauss seidel

    #evento del boton calcular tab de gauss seidel
    def evento_calcular_gauss(e):
        cadena = tab2_row.controls[0].value.replace(" ", "") #capturamos la cadena
        
        #Validamos si la cadena cumple con el farmato valido del sistema de ecuaciones
        if(funciones.verificar_digitos(cadena) and funciones.verificar_combinaciones_invalidas(cadena) and funciones. inicio_fin(cadena) and funciones.cantidad_de_iguales(cadena) and funciones.despues_igual(cadena) and funciones.es_cuadrada(cadena)):
            
            a = funciones.sacar_matrizA(cadena) #Sacamos la matriz A de coeficientes
            b = funciones.sacar_matrizB(cadena) #Sacamos el vector B de terminos independientes

            vector_solucion = funciones.gauss_seidel(a,b) #Obtenemos el vector solucion

            #verificamos si el gauss seidel converge o no
            if type(vector_solucion) == type(0):
                #Si no converge emitimos un mensaje por pantalla 
                tab2_row.controls[1].text_align = "left"
                tab2_row.controls[1].value = "El Gauss Seidel no converge con esa matriz\n\nRecomendaciones: para que el gauss seidel funcione la matriz tiene que ser diagonalmente dominante, es decir , el valor absoluto del elemento diagnola en cada fila es mayor que la suma de los valores absolutos de los otros elementos en esa fila; o la matriz tiene que ser simetrica y definida positivo. Ejemplo:\n\n4,3,2=1\n0,2,1=5\n4,7,15=3\ncuya matriz es diagonalmente dominante"
                page.update()
            else:
                #Si converge mostramos el vector solucion
                tab2_row.controls[1].text_align = "center"
                texto = "Vector Solucion\n"
                for i in range(len(vector_solucion)):
                    texto+= "x" + str(i) + " = " + str(round(vector_solucion[i][0] , 4)) + "\n"
                tab2_row.controls[1].value = texto
                page.update()
        else:
            #Si se ingreso un sistema de ecuaciones no valido con el formato, mostramos un mensaje indicando el formato valido
            dlg = ft.AlertDialog(
                title=ft.Text("Entrada incorrecta, coloca un sistema de ecuaciones cuadrado cuyas entradas de la matriz esten separadas por comas y el termino independiente este separado con un igual, ejemplo:\n\n10,-2,3=1\n2,12.3,8=20\n4,2,9=30\n\nSe admiten tambien numeros negativos y decimales con punto")
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

    #Evecnto boton limpiar del tab de gauss seidel
    def evento_limpiar(e):
        tab2_row.controls[0].value = ""
        tab2_row.controls[1].value = ""
        page.update()


    #Primera fila 
    tab1_row = ft.Row(
        controls=[
            ft.Text("\nEntrada"),
            ft.Text("\n  Salida"),
        ],
        alignment= "center" ,
        spacing= 340,
        
    )

    #Segunda fila
    tab2_row = ft.Row(
        controls=[
            ft.TextField(label="Sistema de Ecuaciones" , multiline=True , min_lines=8 , max_lines=8 , text_align="center" , hint_text="1,0,0=1\n0,1,0=2\n0,0,1=3" ),
            ft.TextField(label="Vector Solucion" , multiline=True , min_lines=8 , max_lines=8 , read_only=True , text_align="center" ) 
        ],
        alignment="center",
        spacing= 100
    )

    #Tercera fila
    tab3_row = ft.Row(
        controls=[
            MyButton(text="Calcular" , on_clicked=evento_calcular_gauss),
            MyButton(text="Limpiar" , on_clicked=evento_limpiar),
        ],
        alignment= "center",
        spacing= 200
    )

    #Agrupo todas las filas en una columa
    tab1_content = ft.Column(
        controls=[
            tab1_row,
            tab2_row,
            ft.Row(controls=[ft.Text("")]), #Agregamos separacion entre la fila 1 y fila 2
            tab3_row
        ]
    )

    #Tab de sistemas numerios

    #Evento del boton calcular de sistemas numericos
    def evento_calcular_sistemas_numericos(e):
        
        cadena = tab2_row_s.controls[0].value.replace("\n" , "") #obtenemos el numero proporcionado por el usario

        #Creamos una alerta por si llega a introducir datos erroneos
        dlg = ft.AlertDialog(
            title=ft.Text("Entrada incorrecta, recuerda colocar solo los numeros correspondientes al sistema numerico seleccionado\n\nNo se admiten numeros negativos ni punto flotantes")
        )

        #Verficamos que tipo de conversion eligio

        if tab3_row_s.controls[1].value == "Binario":

            #Verificamos si introdujo un numero binario valido
            if funciones.es_binario(cadena): 

                decimal = funciones.llevar_decimal(cadena , 2) #Convertimos el numero a decimal

                #Hacemos las converisiones
                texto = "Conversiones numericas\n\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                texto += "Quinario: " + funciones.decimal_quinario(decimal) + "\n"
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Decimal: " + str(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                tab2_row_s.controls[1].value = texto
                page.update()
            else:
                #Mostramos una alerta por introducir el numero mal
                page.dialog = dlg
                dlg.open = True
                page.update()

        elif tab3_row_s.controls[1].value == "Ternario":
            
            #Verificamos si introdujo un numero ternario valido
            if funciones.es_ternario(cadena):

                decimal = funciones.llevar_decimal(cadena , 3) #Convertimos el numero a decimal

                #Hacemos las converisiones
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Quinario: " + funciones.decimal_quinario(decimal) + "\n"
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Decimal: " + str(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                tab2_row_s.controls[1].value = texto
                page.update()
            else:
                #Mostramos una alerta por introducir el numero mal
                page.dialog = dlg
                dlg.open = True
                page.update()

        elif tab3_row_s.controls[1].value == "Quinario":

            #Verificamos si introdujo un numero quinario valido
            if funciones.es_quinario(cadena):

                decimal = funciones.llevar_decimal(cadena , 5) #Convertimos el numero a decimal

                #Hacemos las converisiones
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Decimal: " + str(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                tab2_row_s.controls[1].value = texto
                page.update()
            else:
                #Mostramos una alerta por introducir el numero mal
                page.dialog = dlg
                dlg.open = True
                page.update()
        
        elif tab3_row_s.controls[1].value == "Octal":

            #Verificamos si introdujo un numero binario valido
            if funciones.es_octal(cadena):

                decimal = funciones.llevar_decimal(cadena , 8) #Convertimos el numero a decimal

                #Hacemos las converisiones
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                texto += "Quinario: " + funciones.decimal_quinario(decimal) + "\n"
                texto += "Decimal: " + str(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                tab2_row_s.controls[1].value = texto
                page.update()
            else:
                #Mostramos una alerta por introducir el numero mal
                page.dialog = dlg
                dlg.open = True
                page.update()

        elif tab3_row_s.controls[1].value == "Decimal":

            #Verificamos si introdujo un numero binario valido
            if funciones.es_decimal(cadena):

                decimal = funciones.llevar_decimal(cadena , 10) #Convertimos el numero a decimal

                #Hacemos las converisiones
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                texto += "Quinario: " + funciones.decimal_quinario(decimal) + "\n"
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Hexadecimal: " + funciones.decimal_hexadecimal(decimal)
                tab2_row_s.controls[1].value = texto
                page.update()
            else:
                #Mostramos una alerta por introducir el numero mal
                page.dialog = dlg
                dlg.open = True
                page.update()

        elif tab3_row_s.controls[1].value == "Hexadecimal":

            #Verificamos si introdujo un numero binario valido
            if funciones.es_hexadecimal(cadena):

                decimal = funciones.llevar_decimal(cadena , 16) #Convertimos el numero a decimal

                #Hacemos las converisiones
                texto = "Conversiones numericas\n\n"
                texto += "Binario: " + funciones.decimal_binario(decimal) + "\n"
                texto += "Ternario: " + funciones.decimal_ternario(decimal) + "\n"
                texto += "Quinario: " + funciones.decimal_quinario(decimal) + "\n"
                texto += "Octal: " + funciones.decimal_octal(decimal) + "\n"
                texto += "Decimal: " + str(decimal)
                tab2_row_s.controls[1].value = texto
                page.update()
            else:
                #Mostramos una alerta por introducir el numero mal
                page.dialog = dlg
                dlg.open = True
                page.update()

    #Evento del boton limpiar de sistemas numericos
    def evento_limpiar_sistemas_numericos(e):
        tab2_row_s.controls[0].value = ""
        tab2_row_s.controls[1].value = ""
        page.update()

    #fila 1
    tab1_row_s = ft.Row(
        controls=[
            ft.Text("\nEntrada"),
            ft.Text("\n  Salida"),
        ],
        alignment="center",
        spacing=340
    )

    #fila2
    tab2_row_s = ft.Row(
        controls=[
            ft.TextField(label="Numero" , multiline=True , min_lines=8 , max_lines=8 , text_align="center" , hint_text= "Coloque un numero acorde al sistema numerico seleccionado"),
            ft.TextField(label="Conversiones" , multiline=True , min_lines=8 , max_lines=8 , read_only=True , text_align="left" ) 
        ],
        alignment="center",
        spacing= 100
    )

    #fila 3
    tab3_row_s = ft.Row(
        controls=[
            MyButton(text="Calcular" , on_clicked=evento_calcular_sistemas_numericos),
            ft.Dropdown(
                width=140,
                options=[
                    ft.dropdown.Option("Binario"),
                    ft.dropdown.Option("Ternario"),
                    ft.dropdown.Option("Quinario"),
                    ft.dropdown.Option("Octal"),
                    ft.dropdown.Option("Decimal"),
                    ft.dropdown.Option("Hexadecimal")
                ],
                value="Binario"
            ),
            MyButton(text="Limpiar" , on_clicked=evento_limpiar_sistemas_numericos),
        ],
        alignment= "center",
        spacing= 70
    )

    #Unificamos las filas en una columna
    tab2_content = ft.Column(
        controls=[
            tab1_row_s,
            tab2_row_s,
            ft.Row(controls=[ft.Text("")]),
            tab3_row_s,
        ]
    )


    #Creamos las Tabas
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text= "Gauss Seidel",
                content= tab1_content
            ),

            ft.Tab(
                text="Conversion Numerica",
                content=tab2_content,
             ),
        ],
        expand= 1,
    )

    #Establecemos las dimensiones de la ventana
    page.window_height = 500
    page.window_width = 800
    page.window_resizable = False

    # Centra la ventana en la pantalla
    page.window_center()

    #Añadimos las tabs a la interfaz
    page.add(t)

#Ejecutamos la funcion principal
ft.app(main)