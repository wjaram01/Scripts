# Numericos
edad, _peso = 50, 70.5

#String
nombres = "Javier Jara"
dirDomiciliaria = "Av Mariscal Sucre y Los ceibos"
tipo_sexo="M"

#Boolean
civil = True

#Colecciones
usuario=("Wjaram","1234", "wjaram@unemi.edu.ec")
materias= ["programacion web", "PHP", "POO"]
docente = {"nombre":"Javier", "edad":20, "fac":"faci"}
#imprimir
print("""Mi nombre es {}, tengo {}
amos""".format(nombres,edad))
print(usuario, docente, materias)

#Estructura de control if
x=int(input("Ingresa un numero entero: "))
if x < 0:
    x=0
    print("Negativo cambiado a 0")
elif x == 0:
    print("cero")
elif x == 1:
    print("Uno")
else:
    print("Ninguna opcion")
print("ok") if type(x) == int else print("-")

#Uso while infinito
c = 1
while True:
    print(c)

# while validation
vocal = str(input("Ingrese vocal"))
while vocal not in ("a", "e", "i", "o", "u"):
    if vocal ==".":
        break
    vocal = input("Vocal: ")
print("su vocal o punto es: {}".format(vocal))

# for range(v) -- range(vi,vf)- range (vi, vf, inc)
frase = input("Ingrese frase: ")
for indice in range(len(frase)):
    print(indice,"=", frase[indice])

# for cadena - in(tupla)- in (lista)
for car in frase:
    if car in ('a','e', 'i' , 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        if car in["A","E", "I", "O", "U"]:
            continue
        else:
            cvoc = cvoc + 1
print("cantidad vocales: {}".format(cvoc))

#comprehension - [var for var in datos condicion]
[car for car in["a", 'e', 'o', 'u'] if car not in ["a", "i", "o"]]

