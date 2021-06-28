class cargo:
    secuencia = 0
    def __init__(self, des="Sin cargo"):
        # self.descripcion = ""
        cargo.secuencia = cargo.secuencia+1
        self.codigo = cargo.codigo
        self.descripcion = des


if __name__ == "__main__":
    cargo1 = cargo()
    cargo1.codigo = 1
    cargo1.descripcion = "Docente"
    print(cargo1.codigo, cargo1.descripcion)
    cargo2 = cargo()
    # cargo2.codigo = 2
    cargo2.descripcion = "Director"
    print(cargo2.codigo, cargo2.descripcion)
    cargo3 = cargo("Analista")
    print(cargo3.codigo, cargo3.decripcion)
    print(cargo.secuencia)
    print(cargo.descripcion)
    # print(cargo1.secuencia)
    # print(cargo2.secuencia)
    # print(cargo3.secuencia)