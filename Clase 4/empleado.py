from Cargos import cargo
class empleado:
    def __init__(self,nom,ced,sue,cargo):
        empleado.secuencia = empleado.secuencia+1
        self.codigo = empleado.secuencia
        self.nombre = nom
        self.cedula = ced
        self.sueldo = sue
        self.cargo = cargo
    def mostrar(self):
        print("codigo: {}  nombre: {}   cargo: {}-{}".format(self.codigo, self.nombre, self.codigo, self.des))

    def generarcodigo(self):
        empleado.secuencia = empleado.secuencia +1
        return empleado.secuencia

cargo1 = cargo("docente")
emp1  = empleado("Daniel", "0914", 500, cargo1)
emp1.mostrar()
cargo2 = cargo("Analista")
emp2 = empleado("Ana", "0914", 500, cargo2)
emp2.mostrar()