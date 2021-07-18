class Logica:
    def __init__(self, lista=None):
        self.__lista = lista

    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self):
        self.__lista

    def parImpar(self, num):
        if num % 2 == 0:
            print("El número: {} es Par".format(num))
        else:
            print("El número: {} es Impar".format(num))

    def perfecto(self, num):
        acu = 0
        for contador in range(1, num):
            rec = num % contador
            if rec == 0:
                acu += contador
        if acu == num:
            print("El número: {} es Perfecto".format(num))
        else:
            print("El número: {} no es Perfecto".format(num))


class Ejercicio(Logica):
    def __init__(self, lista, num):
        super().__init__(lista)
        self.dato = num

    def sumar(self, num1, num2):
        return num1 + num2

    def parImpar(self, num):
        super().parImpar(num)
        return num % 2


# ej= Logica([2,4,5])
# ej.lista=[1,3]
# num=int(input("Ingrese un número: "))
# ej.parImpar(num)
# print(ej.lista)
eje = Ejercicio([2, 4, 5], 20)
# print(eje.sumar(4,8))
if eje.parImpar(6) == 0:
    print("Par")
else:
    print("Impar")

print(eje.lista)
eje.perfecto(6)
