#Maria aqui, de una.
#esto es la clase persona pe'
class Persona:
    def __init__(self , nombre = "" , edad = "" , cedula = "") :
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

condicion = True
n = "asaskhjfbksadf"
int("456asd6")
while not n.isnumeric():
    n = input("Coloque el numero de personas: ")
    if not n.isnumeric():
        print("Valor invalido")
n = int(n)
personas = list()

for i in range(n):
    nombre = input("De el nombre de la persona: ")
    edad = input("De la edad de la persona: ")
    cedula = input("De la cedula de la persona: ") 
    personas.append(Persona(nombre , edad , cedula))

for i in range(len(personas)):
    personita = personas[i]
    if personita.es_mayor():
        print(f"{personita.nombre} es mayor de edad")
        print(f"Su edad es: {personita.edad}")
        print(f"Su cedula es: {personita.cedula}")
    

