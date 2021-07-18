class Persona:
    siguiente = 0

    def __init__(self, nombre="Invitado", activo=True):
        self.__codigo = self.siguiente()
        self.__nombre = self.__nombreMayus(nombre)
        self.activo = activo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def codigo(self):
        return self.__codigo

    @nombre.setter
    def codigo(self, cod):
        self.__codigo = cod

    def siguiente(self):
        Persona._siguiente = Persona._siguiente + 1
        return Persona._siguiente

    def __nombreMayus(self, nomb):
        return nomb.upper()


pers1 = Persona()
print(pers1.nombre)
pers2 = Persona("Daniel", False)
print(pers2.nombre, pers2.activo)