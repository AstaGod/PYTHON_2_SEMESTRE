from rich import print
# from rich.markdown import Markdown
# edad=20
# respuesta="[bold blue]es mayor de edad" if edad>17 else "[italic underline red]es menor de edad"
# texto="""
#     # titulo
#     parrafo
#     ```bash
#     git commit -m "titulo" -m "cuerpo del commit"
#     # comentario
#     ```
#     # lista
#     # lista
#     > informacion valiosa
# """
# print(respuesta)
# mostrar_mark=Markdown(texto)
# print(mostrar_mark)

# Repaso de programacion orientada a objetos
# class Mascota:
#     # atributos de instancia
#     def __init__(self):# self para asociar el methodo con la clase
#         self.nombre=None
#         self.edad=None
#         self.tipo_animal=None
#     # methodos -> funciones o acciones que puede realizar mi clase
#     def hablar(self,sonido):
#         return sonido
#     def datos_mascota(self,nombre,edad,tipo_animal):
#         self.nombre=nombre
#         self.edad=edad
#         self.tipo_animal=tipo_animal

# # instanciar una clase me refiero a crear un objeto
# # como se instancia alamcenando en una variable la clase
# class Perro(Mascota):
#     def atacar(self):
#         return "ladra y muerde"
# class Gato(Mascota):
#     pass

# perro_boby=Perro()
# perro_boby.datos_mascota("boby",14,"perro")
# print(f"[bold blue]"+perro_boby.hablar('guauuu guauu'))
# print("[bold blue]"+perro_boby.atacar())
# print("[bold blue]"+perro_boby.nombre+' '+perro_boby.tipo_animal)

# class Persona:
#     def __init__(self,nombre:str,sexo:str,edad:int,dni:int):
#         self.nombre=nombre
#         self.sexo=sexo
#         self.edad=edad
#         self.dni=dni

#     def habla(sefl,sonido1:str):
#         return sonido1
#     def come(self,comer:str):
#         return comer
    
# class Estudiante(Persona):
#     def __init__(self, nombre: str, sexo: str, edad: int, dni: int,carrera_profesional:str):
#         super().__init__(nombre, sexo, edad, dni)
#         self.carrrera_profesional=carrera_profesional

#     def estudiar(self):
#         return "estoy estudiando POO"

# class Trabajador(Persona):
#     def __init__(self, nombre: str, sexo: str, edad: int, dni: int,profesion:str):
#         super().__init__(nombre, sexo, edad, dni)
#         self.profesion=profesion
    
#     def trabajar(self):
#         return " estoy en mi trabajo"

# jhona=Estudiante("jhonatan henry","masculino",18,71458988,"Arquitectura")
# print(f"[bold blue]"+jhona.habla('hola causa'))
# print("[bold blue]"+jhona.come("cebiche"))
# print("[bold blue]"+jhona.estudiar())
# print("[bold blue]"+jhona.nombre)

class Vehiculo:
    def __init__(self,marca:str,modelo:str,color:str,ruedas:int):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.ruedas=ruedas

    def prender(self,motor_prende):
        return motor_prende

    def apagar(self):
        return "se apago el auto"

    def avanzar(self):
        return "el auto esta en movimiento"

    def retroceder(self):
        return "el autos esta marcha atraz"
class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, color: str, ruedas: int,rpm:int):
        super().__init__(marca, modelo, color, ruedas)
        self.rpm=rpm

    def nitro(self):
        return "nitro x10 activado"

class Omnibus(Vehiculo):
    def __init__(self, marca: str, modelo: str, color: str, ruedas: int,num_asientos:int):
        super().__init__(marca, modelo, color, ruedas)
        self.num_asientos=num_asientos
    
    def recojer_pasajero(self):
        return "parando en la parada y recojiendo positivas"

lambo=Auto("lamborguini","veneno","dorado",4,8400)
print(f"[bold blue]"+lambo.prender("encedido con llave"))
print("[bold blue]"+lambo.avanzar())
print("[bold blue]"+lambo.retroceder())
print("[bold blue]"+lambo.apagar())
print("[bold blue]"+lambo.nitro())

omnibus_palomino=Omnibus("mercedes","0500 RSD","blaco y verde",18,60)
print(f"[bold blue]"+omnibus_palomino.prender("encedido con llave"))
print("[bold blue]"+omnibus_palomino.avanzar())
print("[bold blue]"+omnibus_palomino.retroceder())
print("[bold blue]"+omnibus_palomino.apagar())
print("[bold blue]"+omnibus_palomino.recojer_pasajero())