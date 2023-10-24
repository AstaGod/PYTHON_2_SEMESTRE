# crear un sistema para gestion de stock de productos
# Caso de Uso
# Historias de Usuario
# Producto Ower
# Baclog
# MVP
# Prototipos de Mierda

# averiguar fomras normales (normalizacion de base de datos)
# entidad entitis
# la base de datos sobre la que voy a trabajar
productos=[
    {
        "id":"1",
        "codigo":"2023-A",
        "nombre":"arroz",
        "descripcion":"costeño costal x 100 kg",
        "stock":5,
        "unidad":"costales",
        "precio":125,
        "moneda":"soles"
    }
]

# casos de uso
class Producto:
    # atributos de instancia
    def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda
    # creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""tienes {len(productos)} productos los productos son: {productos}"""
        return mensaje
    
    def registrar_producto(self):
        nuevo_id=len(productos)+1
        codigo="2023-B"
        producto_nuevo={
            "id":nuevo_id,
            "codigo":codigo,
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "stock":self.stock,
            "unidad":self.unidad,
            "precio":self.precio,
            "moneda":self.moneda
        }
        registro_producto=productos.append(producto_nuevo)
        return f"el siguiente producto se registro exitosamente{producto_nuevo}"
    
    def mostrar_producto(self,id):
        producto_buscar=productos[id-1]
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminar=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminar}"
    
    # def actualizar_producto(self,id,clave,valor):
    #     producto_actualizar=list(filter(lambda obj: obj[clave]==id,productos)) #["h","o","l","a"]
    #     return producto_actualizar
        #list funcion para crear lista

    def actualizar_producto(self,id,clave,valor):
        el=valor
        producto_actualizar=list(filter(lambda el: el[clave]==id,productos))[0].update({clave:valor}) #["h","o","l","a"]
        return "se actualizo"

# programacion funcional en python
# metodo funcional filter retona una lista con el elemento que se true de una lista
# funciones anonimas o autoejecutadas en python se les conoce como funciones lambda -> una funcion anonima
# su uso estructura
# lambda a,b:return a+b # esta funcion se autoejecuta no se llama
# suma=lambda a,b: retun a+b # para erar esta funcion necesita llamar al variable suma
# suma(3,7)

prod=Producto("aceite","extra virgen",2,"botella litro",12.50)
print(prod.registrar_producto())
print(prod.mostrar_productos())
# print(prod.mostrar_producto(1))
# print(prod.eliminar_producto(2))
# print(prod.mostrar_productos())
print(prod.actualizar_producto(125,"precio",130))
print(prod.mostrar_productos())

# Ejercicio 2

# personas=[
#     {
#         "id":"1",
#         "DNI":71439102,
#         "nombre":"Crhistian",
#         "apellido":"Bautista Poma",
#         "edad":17,
#         "altura":1.70,
#         "sexo":"masculino",
#     }
# ]

# # casos de uso
# class Alumno:
#     # atributos de instancia
#     def __init__(self,DNI,nombre,apelliido,edad,altura,sexo):
#         self.DNI=DNI
#         self.nombre=nombre
#         self.apellido=apelliido
#         self.edad=edad
#         self.altura=altura
#         self.sexo=sexo
#     # creacion de metodos
#     def mostrar_alumnos(self):
#         mensaje=f"""los datos del alumno son: {personas}"""
#         return mensaje
    
#     def registrar_nuevo_alumno(self):
#         nuevo_id=len(personas)+1
#         alumno_nuevo={
#             "id":nuevo_id,
#             "DNI":self.DNI,
#             "nombre":self.nombre,
#             "apellido":self.apellido,
#             "edad":self.edad,
#             "altura":self.altura,
#             "sexo":self.sexo
#         }
#         registro_nuevo_alumn=personas.append(alumno_nuevo)
#         return f"el siguiente alumno se registro exitosamente {alumno_nuevo}"
    
#     def mostrar_alumno(self,id):
#         alumno_buscar=personas[id-1]
#         return alumno_buscar
    
#     def eliminar_alumno(delf,id):
#         alumno_eliminar=personas.pop(id-1)
#         return f"el siguiente alumno fue eliminado {alumno_eliminar}"
    
#     def actualizar_alumno(self,id):
#         pass

# alumn=Alumno(72548931,"orlando","virgen",19,1.80,"masculino")
# print(alumn.registrar_nuevo_alumno())
# print(alumn.mostrar_alumnos())
# print(alumn.mostrar_alumno(1))
# print(alumn.eliminar_alumno(2))
# print(alumn.mostrar_alumnos())