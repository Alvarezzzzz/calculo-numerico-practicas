def es_primo(a):
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

def numeros_primos(a,b):
    numeros = list()
    if a>b:
        temp = a
        a = b
        b = temp
    for i in range(a+1,b):
        if es_primo(i):
            numeros.append(i)
    if len(numeros) != 0:
        print(f"Entre los numeros {a} y {b} hay {len(numeros)} primos, que son:")
        cosa = list( str(i) +"," if i != numeros[len(numeros)-1] else str(i) for i in numeros)
        print("".join(cosa))
    else:
        print(f"Entre los numeros {a} y {b} no hay numeros primos:")

x = int(input("Intruduce un numero: "))
y = int(input("Intruduce otro numero: "))
numeros_primos(x,y)