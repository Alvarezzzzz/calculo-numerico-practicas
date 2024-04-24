#Comentario desde repo local
class Persona:
    def __init__(self , nombre = "" , edad = 0 , cedula = "") :
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_cedula(self):
        return self.cedula
    
    def set_nombre(self , nombre):
        self.nombre = nombre

    def set_cedula(self , cedula):
        self.cedula = cedula
    
    def set_edad(self , edad):
        self.edad = edad
    
    def es_mayor(self):
        return self.edad >=18

n = "asaskhjfbksadf"
while not n.isnumeric():
    n = input("Coloque la cantidad de personas: ")
    if not n.isnumeric():
        print("Valor invalido")
n = int(n)
personas = list()

for i in range(n):
    while True:
        nombre = input("De el nombre de la persona: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Nombre incorrecto")
    
    try:
        edad = int(input("De la edad de la persona: "))
    except ValueError:
        print("Valor de edad incorrecto")
        edad = 0
    while True:
        cedula = input("De la cedula de la persona: ") 
        cedula = cedula.replace("," ,"").replace("." , "").replace(" " , "")
        if all(digito.isdigit() for digito in cedula):
            break
        else:
            print("Cedula mala, vuelve a colocarla")
    
    personas.append(Persona(nombre , edad , cedula))

for i in range(len(personas)):
    personita = personas[i]
    if personita.es_mayor():
        print(f"{personita.nombre} es mayor de edad")
        print(f"Su edad es: {personita.edad}")
        print(f"Su cedula es: {personita.cedula}")
    

