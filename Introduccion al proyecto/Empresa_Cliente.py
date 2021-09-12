from datetime import date

class Empresa:
    def __init__(self, nombre,ruc, tele,direccion):
        self.nombre= nombre
        self.ruc= ruc
        self.telefono= tele
        self.direccion= direccion
    
    def mostrarEmpresa(self):
        print("Empresa: {:20} Ruc: {}".format(self.nombre, self.ruc))

from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, cedul, nombre, direccion, tele):
        self.cedula= cedul
        self.nombre= nombre
        self.direccion= direccion
        self.telefono= tele

    def mostrarCliente(self):
        print("Cliente: {:17} Cedula: {:17} ".format(self.nombre, self.cedula))
    
    @abstractmethod
    def getCedula(self):
        return self.cedula
    
class ClienteCorporativo(Cliente):
    def __init__(self,cedul, nombre, direccion, tele,contrato):
        super().__init__(cedul, nombre, direccion, tele)
        self.__contrato= contrato
        
    @property 
    def contrato(self):   #getter: obtener el valor del atributo privado
        return self.__contrato
    
    @contrato.setter
    def contrato(self,value):    #setter: asigna un valor al atributo privado
        if value:
            self.__contrato= value
        else:
            self.__contrato= "Sin contrato"

    def mostrarCliente(self):
        print("Cliente: {:17} Contrato: {}".format(self.nombre, self.__contrato))

class ClientePersonal(Cliente):
    def __init__(self,cedul, nombre, direccion, tele,promocion= True):
        super().__init__(cedul, nombre, direccion, tele)
        self.__promocion= promocion
        
    @property 
    def promocion(self):   
        return self.__promocion

    def mostrarCliente(self):
        print("Cliente: {:17} Cedula:{} Promoción: {}".format(self.nombre, self.cedula, self.promocion))
    
    def getCedula(self):
        return super().getCedula()

class Articulo:
    
    secuencia=0
    iva=0.12
    
    def __init__(self, des,pre,sto):
        Articulo.secuencia+=1
        self.codigo= Articulo.secuencia
        self.descripcion= des
        self.precio= pre
        self.stock= sto
    
    def mostrarArticulo(self):
        print(self.codigo, self.descripcion, self.precio, self.stock)

class detVenta:
    linea=0

    def __init__(self, articulo, cantidad):
        detVenta.linea+=1
        self.lineaDetalle=detVenta.linea
        self.articulo= articulo
        self.precio= articulo.precio
        self.cantidad= cantidad
    
class cabVenta:
    def __init__(self, fac, fecha,cliente, tot=0):
        self.factura= fac
        self.fecha= fecha
        self.cliente= cliente
        self.total= tot
        self.detVen= []
    
    def agregarDetalle(self,articulo, cantidad):
        detalle= detVenta(articulo,cantidad)
        self.total+=detalle.precio*detalle.cantidad
        self.detVen.append(detalle)
    
    def mostrarVenta(self, empNombre, empRuc):
        print("Empresa: {:17} Ruc: {}" .format(empNombre, empRuc))
        print("Factura: {:17} Fecha: {}" .format(self.factura, self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo        Precio  Cantidad  Subtotal ")
        for det in self.detVen:
            print("{:5} {:15} {} {:6} {:7}" .format(det.linea, det.articulo.descripcion, det.precio, det.cantidad, det.precio*det.cantidad))
        print("Total Venta: {:26}" .format(self.total))

# emp= Empresa("El mas Barato", "099999999", "042971234", "Juan Montalvo y Pedro Carbo")
# cli1= ClientePersonal("09471510245","Carlos Garcia", "Cdla. Las Piñas","0988318480",True)
# print(cli1.getCedula())
# cli1.mostrarCliente()
# art1= Articulo("manzana",1,200)
# art1.mostrarArticulo()
# art2= Articulo("manzana",1,200)
# art2.mostrarArticulo()
# print(Articulo.iva)
# today= date.today()
# fecha= date(2021,9,11)
# venta= cabVenta("F0001", date.today(), cli1)
# venta.agregarDetalle(art1,2)
# venta.agregarDetalle(art2,3)
# venta.mostrarVenta(emp.nombre, emp.ruc)

class InterfaceSistemaPago(ABC):
    @abstractmethod
    def pago(self):
        pass

    @abstractmethod
    def saldo(self):
        pass

class PagoTarjetaImplements(InterfaceSistemaPago):
    def pago(self):
        return "Pago tarjeta"
    
    def saldo(self):
        return "Saldo Tarjeta rebajado"

class ImplementsPagoContrato(InterfaceSistemaPago):
    def pago(self):
        return "Pago Contrato2"
    
    def saldo(self):
        return "Saldo Contrato rebajado"

class Vendedor:
    def __init__(self, nom):
        self.nombre= nom
    
    def moduloPago(self,contratoV):
        return contratoV.pago()

pagoTarjeta= PagoTarjetaImplements()
print(pagoTarjeta.pago())
pagoContrato= ImplementsPagoContrato()
print(pagoContrato.pago())
ven= Vendedor("Daniel")
print(ven.moduloPago(pagoContrato))

