class Condicion:
    contador = 0  # variable de clases(opcional)
    # __init__ Metodo constructor que se ehecuta cuando se instancia la clase cuyo objeto es crear
    # e inicializar ls atributos de la clase. Self es un objeto que representa

    def __init__(self, num1=0, num2=0):
        self.numero1 = num1
        self.numero2 = num2

    def uso_if(self):
        if self.numero1 == self.numero2:
            print("num1:{}, num2:{}  SOn iguales".format(self.numero1, self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1:{},numero3:{} son iguales".format(self.numero1, self.numero2))
        else: print("No son iguales")

# usar clase
cond1 = Condicion()
print(cond1.numero1)
print(cond1.numero2)

cond1 = Condicion(10,20)
print(cond1.numero1)
print(cond1.numero2)