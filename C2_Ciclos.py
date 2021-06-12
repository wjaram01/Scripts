class Ciclos:
    def __init__(self, num1=0):
        self.numero1 = num1

    def usowhile(self):
        # ciclo repetitivo que se ejecuta por verdadero y sale por falso
        car = input("Ingrese una vocal")
        car = car.lower()
        while car not in ("a", "e", "i", "o", "u"):
            car = input("Ingrese una vocal: ").lower
        print("felicitaciones el caracter: {}  es una vocal".format(car))


ciclo1 = Ciclos()
ciclo1.usowhile()
