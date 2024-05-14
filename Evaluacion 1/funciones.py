import numpy as np

#Verigicamos que la cadena solo tenga digitos numericos, la coma , el igual y el punto
def verificar_digitos(cadena):
    caracteres_permitidos = "1234567890,=-."
    for caracter in cadena.replace("\n" , ""):
        if caracter not in caracteres_permitidos:
            print("hola0")
            return False
    return True


#Verificamos que no hayan combinaciones invalidads
def verificar_combinaciones_invalidas(cadena):
    cadena = cadena.replace(" " , "")
    if ",," in cadena:
        return False
    elif ",=" in cadena:
        return False
    elif ",." in cadena:
        return False
    elif "==" in cadena:
        return False
    elif "=," in cadena:
        return False
    elif "=." in cadena:
        return False
    elif "--" in cadena:
        return False
    elif "-," in cadena:
        return False
    elif "-=" in cadena:
        return False 
    elif "-." in cadena:
        return False 
    elif ".." in cadena:
        return False 
    elif ".=" in cadena:
        return False 
    elif ".-" in cadena:
        return False 
    elif ".," in cadena:
        return False 
    elif "0-" in cadena:
        return False 
    elif "1-" in cadena:
        return False 
    elif "2-" in cadena:
        return False 
    elif "3-" in cadena:
        return False 
    elif "4-" in cadena:
        return False 
    elif "5-" in cadena:
        return False 
    elif "6-" in cadena:
        return False 
    elif "7-" in cadena:
        return False 
    elif "8-" in cadena:
        return False 
    elif "9-" in cadena:
        return False 
    return True

#verifica si la cadena no inicia o termina con un caracter invalido
def inicio_fin(cadena):
    lineas = cadena.replace(" ", "").split("\n")
    for linea in lineas:
        if(linea == ""):
            print("hola6")
            return False
        else:
            if linea[0] == "," or linea[0] == "=" or linea[0] == "."  or linea[len(linea) -1] == "," or linea[len(linea) -1] == "=" or linea[len(linea) -1] == "-" or linea[len(linea) -1] == "." :
                print("hola4")
                return False
    return True

#Verifica que por cada columna hay un solo igual
def cantidad_de_iguales(cadena):
    lineas = cadena.replace(" ", "").split("\n")
    for linea in lineas:
        if str(linea).count("=") != 1:
            print("hola")
            return False
    return True

#verifica que despues del igual solo haya el termino independiente
def despues_igual(cadena):
    lineas = cadena.replace(" ", "").split("\n")
    for linea in lineas:
        if "," in linea[str(linea).index("="):] :
            print("hola2")
            return False
    return True

#Verifica que la matriz sea cuadrada
def es_cuadrada(cadena):
    lineas = cadena.replace(" ", "").split("\n")
    tamaño_columnas = len(lineas[0].split(","))
    tamaño_filas = len(lineas)
    if tamaño_columnas != tamaño_filas:
        print("hola5")
        return False
    for linea in lineas:
        fila = linea.split(",")
        if(tamaño_columnas != len(fila)):
            print("hola3")
            return False
    return True

#Saca la matriz A de coeficientes de la cadena
def sacar_matrizA(cadena):
    lineas = cadena.replace(" " , "").split("\n")
    a = list()
    for linea in lineas:
        b = list()
        fila = linea.split(",")
        fila[len(fila) - 1] = fila[len(fila) - 1][0: fila[len(fila) - 1].index("=")]
        for i in fila:
            b.append(float(i))
        a.append(b)
    return a

#Saca la matriz B de terminos independientes de la cadena
def sacar_matrizB(cadena):
    lineas = cadena.replace(" " , "").split("\n")
    a = list()
    for linea in lineas:
        elemento = linea[linea.index("=")+1:]
        a.append(float(elemento))
    return a

#Aplica el gauss seidel, a una matirz a y un vector b, y retorna el vector solucion
def gauss_seidel(a,b):

    #Creamos la matriz de coeficientes, de terminos independientes y el vector solucion 
    A = np.array(a)
    B = np.array(b)
    XO = np.zeros((len(b)))

    #Establecemos la tolerancia y la iteracion maxima
    tolera = 0.00001
    iteramax = 100

    #Procedimiento
    tamano = np.shape(A) #captumramos las dimensiones del arreglo A
    n = tamano[0]
    m = tamano[1]

    #  valores iniciales
    X = np.copy(XO)
    diferencia = np.ones(n, dtype=float) #Creamos un arreglo de n elementos de puros 1
    errado = 2*tolera

    itera = 0

    while not(errado<=tolera or itera>iteramax):
        # por fila
        for i in range(0,n,1):
            # por columna
            suma = 0 
            for j in range(0,m,1):
                # excepto diagonal de A
                if (i!=j): 
                    suma = suma-A[i,j]*X[j]
        
            nuevo = (B[i]+suma)/A[i,i]
            diferencia[i] = np.abs(nuevo-X[i])
            X[i] = nuevo
        errado = np.max(diferencia)
        itera = itera + 1

    # Respuesta X en columna
    X = np.transpose([X]) #le sacamos la traspuesta a X

    # revisa si NO converge
    if (itera>iteramax):
        return 0
    return X

#verifica si la cadena es un numero binario valido
def es_binario(cadena):
    for i in cadena:
        if i not in "01":
            return False
    return True

#verifica si la cadena es un numero ternario valido
def es_ternario(cadena):
    for i in cadena:
        if i not in "012":
            return False
    return True

#verifica si la cadena es un numero quinario valido
def es_quinario(cadena):
    for i in cadena:
        if i not in "01234":
            return False
    return True

#verifica si la cadena es un numero octal valido
def es_octal(cadena):
    for i in cadena:
        if i not in "01234567":
            return False
    return True

#verifica si la cadena es un numero decimal valido
def es_decimal(cadena):
    for i in cadena:
        if i not in "0123456789":
            return False
    return True

#verifica si la cadena es un numero hexadecimal valido
def es_hexadecimal(cadena):
    for i in cadena:
        if i not in "0123456789ABCDEFabcdef":
            return False
    return True

#Lleva a decimal un numero de cuya base es proporcionada
def llevar_decimal(numero , base):
    decimal = 0
    n = len(numero)-1
    if base == 16:
        for digito in numero:
            if digito == "A" or digito == "a":
                digito = 10
            elif digito == "B" or digito == "b":
                digito = 11
            elif digito == "C" or digito == "c":
                digito = 12
            elif digito == "D" or digito == "d":
                digito = 13
            elif digito == "E" or digito == "e":
                digito = 14
            elif digito == "F" or digito == "f":
                digito = 15
            decimal += int(digito)*base**n
            n-=1
    else:
        for digito in numero:
            decimal += int(digito)*base**n
            n-=1
    return decimal


#Convierte decimal a binario
def decimal_binario(numero):
    return bin(numero).replace("0b" , "")

#Convierte decimal a ternario
def decimal_ternario(numero):
    if numero == 0:
        return "0"
    ternario = ""
    while numero>0:
        ternario = str(numero%3) + ternario
        numero//=3
    return ternario

#Convierte decimal a quinario
def decimal_quinario(numero):
    if numero == 0:
        return "0"
    quinario = ""
    while numero>0:
        quinario = str(numero%5) + quinario
        numero//= 5
    return quinario

#Convierte decimal a octal
def decimal_octal(numero):
    return oct(numero).replace("0o", "")

#Convierte decimal a hexadecimal
def decimal_hexadecimal(numero):
    return hex(numero).replace("0x", "")

