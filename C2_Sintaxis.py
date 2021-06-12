num=2
if type(num)==int:
    print("respuesta", num*2)
else:
    print("El dato no es numerico")

def mensaje(men):
    print(men)

mensaje("Mi primer programa")
mensaje("Mi segundo programa")


#class Sintaxis:
    #def useVariables(self):
        #edad, _peso = 50, 70.50


#ejer1 = Sintaxis()
#ejer1.useVariables()

class Sintaxis:
    instancia = 0 # variables de clases
    # __init__ Metoo constructor que se ejecura cuando se instancia la lase cuyo objetivo es
    # e inicializar los atributos de la clase, Self es un objeto que representa la clase creada
    def __init__(self, dato="Inicializacion"):
        self.frase = dato # variables de instancia
        #Sintaxis.instancia = Sintaxis.Instancia+1

    # def usoVariables(self):
    #     edad, _peso = 50, 70.5
    #     nombres = "Walter jara"
    #     tipo_sexo = "M"
    #     civil = True
    #     print(nombres, edad)

# ejer1 = Sintaxis() #se crea un objeto que es una instancia de la clase
# ejer1.usoVariables()
# print(ejer1.frase)

    def usoVariables(self):
        edad, _peso = 50, 70.5
        nombres = "Walter jara"
        tipo_sexo = "M"
        civil = True
        # tuplas = () son colecciondes de datos de cualquier tipo inmutables
        usuario=()
        usuario=("Wjaram",1234, "Wjaram@unemi.edu.ec", True)
        #usuario[3]="milagro"
        # listas = [] colecciones mutables
        materias = []
        materias = ["Programacion web", "PHP", "POO"]
        materias[1]= "Python"
        materias.append("Go")
        # diccionario = {} coleccioones de objetos clave: valor tipo json
        docente = []
        docente = {"nombre":"Daniel","edad":50, "fac":"faci"}
        docente ["carrera"] = "CS"
        # #presentacion con format
        # print("""Mi nombres es {}, tengo {}
        # anos""".format(nombres, edad))
        #print(usuario, materias, docente)
        print(usuario,usuario[0], usuario[0:2], usuario[-1])
        #print(materias, materias[2:}, materias[:1], materias[::], materias[-2:])
        #print(docente, docente["nombre"])


ejer1 = Sintaxis() #se crea un objeto que es una instancia de la clase
ejer1.usoVariables()
print(ejer1.frase)
