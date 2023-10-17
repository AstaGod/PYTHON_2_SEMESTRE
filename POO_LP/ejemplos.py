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
        producto_nuevo={
            "id":nuevo_id,
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
    
    def eliminar_producto(delf,id):
        producto_eliminar=productos.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminar}"
    
    def actualizar_producto(self,id):
        pass

prod=Producto("aceite","extra virgen",2,"botella litro",12.50)
print(prod.registrar_producto())
print(prod.mostrar_productos())
print(prod.mostrar_producto(1))
print(prod.eliminar_producto(2))
print(prod.mostrar_productos())