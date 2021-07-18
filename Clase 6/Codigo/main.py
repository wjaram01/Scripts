
class Articulo:
    def __init__(self, cod, des, pre, sto):
        self.codigo = cod
        self.descripcion = des
        self.precio = pre
        self.stock = sto


class Cliente:
    def __init__(self, ced, nom, dirc, tel):
        self.cedula = ced
        self.nombre = nom
        self.direccion = dirc
        self.telefono = tel


class Venta:
    def __init__(self, fac, fec, cliente, tot, detalle):
        self.factura = fac
        self.fecha = fec
        self.cliente = cliente
        self.total = tot
        self.detalle = detalle


class VentaDet:
    def __init__(self, articulo, precio, cantidad):
        self.articulo = articulo
        self.precio = precio
        self.cantidad = cantidad
