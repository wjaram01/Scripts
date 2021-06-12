# FUNCIONES SIN RETORNO
def vocales(frase):
    for car in frase:
        if car in ("a", "e", "i", "i", "o", "u"):
            print(car)

# LLAMADA DE FUNCION

oracion = input("Ingrese oracion: ")
vocales(oracion.lower())

# FUNCION CON RETORNO DE VALOR

def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)

# LLAMADA A FUNCION
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
print("Promedio: ()".format(listanotas, prom))

# Funciones Matematicas
import math
num1, num2, num, men = 12.572, 15.4, 4, "1234"
print(math.ceil(num1),"\t", math.floor(num1))
print(round(num1,1),"\t",type(num), "\t", type(men))

#Funciones de Cadena
mensaje = "Hola" + "mundo" + "Python"
men1 = mensaje.split()
men2 = "".join(men1)
print(mensaje[0], mensaje[0:4], men1, men2)
print(mensaje.find("mundo"), mensaje.lower())

#Funciones de Fecha
from datetime import datetime, timedelta, date
hoy, fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days = 30)
dif, aa, mm, dd = futuro - hoy, hoy.year, hoy.month, hoy.day
fecha = date(aa, mm, dd+2)
print(hoy. fdia, futuro, dif, fecha)