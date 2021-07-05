class Operaciones:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2

    def suma(self):
        suma = self.numero1 + self.numero2
        return suma

    def resta(self):
        if self.numero1 >= self.numero2:
            return self.numero1 - self.numero2
        return 0

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2 != 0 : return self.numero1 / self.numero2
        return 0

    def division_entera(self):
        if self.numero2 != 0 : return self.numero1 // self.numero2
        return 0

    def exponente(self):
        return self.numero1 ** self.numero2

    def  residuo(self):
        return self.numero1 %self.numero2

# operacion = Operaciones(10,20)
# x = operacion.suma()
# # print(operacion.suma())
# # print(operacion.division())
# y = operacion.resta()
# z = x ** y
# print(z)
# operacion.mostrar()
print("Menu opciones matematicas")
print("1) Suma\n2)Resta\n3)Mltiplicacion\n4)Division\n5)Division\nentera\n6)Residuo\n7)Exponente\n8)salir")

opc = "0"
while opc !=8:
    opc = input("Elija opcion [1...8]")
    num1 = float(input("ingrese el primer numero:"))
    num2 = float(input("ingrese el segundo numero:"))
    if opc == "1":
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        ope = Operaciones(num1, num2)
        print("{}+{} = {}.".format(num1, num2, ope.suma()))
    elif opc == "2":
        ope = Operaciones(num1, num2)
        print("{}-{} = {}.".format(num1, num2, ope.resta()))

    elif opc == "3":
        ope = Operaciones(num1, num2)
        print("{}-{} = {}.".format(num1, num2, ope.resta()))\

    elif opc == "4":
        ope = Operaciones(num1, num2)
        print("{}-{} = {}.".format(num1, num2, ope.resta()))

print("Gracias por su visita")