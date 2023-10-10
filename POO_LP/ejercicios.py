# haciendo uso de la POO crear un objeto para entidad celular
class Celular:
    marca="Samsumng"
    tamaño="163.3,77.3"
    color="negro"
    pantalla="super amoled"

    def enceder_celular(self):
        return "mantiene presionado el boton encender"
    
    def mensaje(self):
        return "escribir y recibir mensajes de texto"
    
print(Celular.marca)
# haciendo uso de la POO crear un objeto para entidad vehiculo
class Vehiculo:
    marca="Lanborguini"
    motor="10000000 caballos de fuerza"
    color="dorado"
    asientos=2

    def avanzar(self):
        return "recorriste 10 km"
    
    def estacionar(self):
        return "te estasionaste en el lugar 7"
    
print(Vehiculo.color)
# haciendo uso de la POO crear un objeto para entidad avion
class avion:
    color="blanco"
    motores=2
    ruedas=20

    def vuela(self):
        return "despejo de la line a de aterrisaje"
    
    def aterriza(self):
        return "se aterrizo con exito en el aeropuerto"
print(avion.color)
# haciendo uso de la POO crear un objeto para un heroe de dota2
class heroe:
    nombre="Jinx"
    rol="tirador"
    edad=19

    def habilidad_pasiva(self):
        return "gran aumento de velocidad de movimiento y velocidad de ataque"
    
    def habilidad_q(self):
        return "¡Cambiazo!: Jinx modifica sus ataques básicos al alternar entre Pium Pium, su ametralladora, y Espinas, su lanzacohetes."
    
    def habilidad_w(self):
        return "¡Zap!: Jinx usa a Chispita, su pistola de rayos, para disparar un rayo que ralentiza e inflige daño al primer enemigo que golpea, revelándolo."
    
    def habilidad_e(self):
        return "¡Mascafuegos!: Jinx lanza una hilera de granadas paralizantes que explotan tras 5 s y envuelven en llamas a los enemigos circundantes."
    
    def habilidad_r(self):
        return "¡Supermegacohete mortal!: Jinx dispara un supercohete por todo el mapa que va aumentando su daño a medida que avanza"

print(heroe.nombre)

# haciendo uso de la POO crear un objero para una pc
class pc:
    componentes="Monitor, Case, Teclado, etc"
    color="rgb"

    def prender(self):
        return "presionar el boton de encendidio"
    def teclado(self):
        return "escribir en el teclado"
    
print(pc.componentes)
# haciendo uso de la POO crear un objero para una impresora
class impresora:
    color="negro"
    tinta="negro, azul, rojo, etc"

    def imprimir(self):
        return "imprimi una hoja"
    def escan(self):
        return "escanea una imagen o documento"
    def momnocromatica(self):
        return "solo imprime en color negro"
print(impresora.tinta)
# haciendo uso de la POO crear un objero para emitir una factura
class factura:
    nombre="nombre del cliente"
    DNI="4454564654"

    def agreagar_p(self):
        return "agregar producto"
    def igv(self):
        return "sacar el igv"
    
print(factura.nombre)

# 1. crear un objeto laptop con dos atributos de clase y 5 atributos de instancia devera tener hasta 3 funcionalidades como minimo

# crear tres objetos instancia de clase distrinstos
# # ojo: solo utilizar lo que hemos echo en clase
class Laptop:
    tamaño="16.5 pulgadas"
    laptop="computadora portatil"

    def __init__(self,marca,modelo,procesador,almacenamiento,RAM):
        self.marca=marca
        self.modelo=modelo
        self.procesador=procesador
        self.almacenamiento=almacenamiento
        self.RAM=RAM

    def jugar(self,juegos):
        return f"esta jugando {juegos}"

# objeto 1
lapcris=Laptop("Asus","Rog Strix G713RM-LL046W","Ryzen 9 6900HX ","1 TB","16GB")
print(lapcris.marca)
print(lapcris.procesadeor)
print(lapcris.jugar("Minecraft"))
# objeto 2
laphans=Laptop("hp","V15 Gen 2 ","Core i7 1165G7 ","500GB","8GB")
print(laphans.marca)
print(laphans.procesadeor)
print(laphans.jugar("Pou"))
# objeto 3
lapjona=Laptop("Dell","Inspiron 15 3511 ","Intel Core i5 1135G7","500GB","8GB")
print(lapjona.marca)
print(lapjona.procesadeor)
print(lapjona.jugar("Free Fire"))

# crear una clase mercado que tengta un atributo de clase 5 atributos de instancia y funcionalidades
#devera crear 4 instancia de la clase mescado
#ejm puesto mechita, puesto la gringa, puesto ojo de uva
class Mercado:
    medida="32m"

    def __init__(self,nombre_puesto,sexo,color,tipo_de_puesto,productos):
        self.nombre_puesto=nombre_puesto
        self.sexo=sexo
        self.color=color
        self.tipo_de_puesto=tipo_de_puesto
        self.productos=productos

    def abrir_puerta(self,nombre):
        return f"el cliente {nombre} entro"
    
    def compro(self,client,product):
        return f"{client} compro este producto: {product}"
    
    def salir(self,client):
        return f"el client {client} salio por la puerta"
    
# objeto 1
clientvirgen=Mercado("puesto mechita","femeninio","azul","comida","cebiche")
print(clientvirgen.tipo_de_puesto)
print(clientvirgen.productos)
print(clientvirgen.abrir_puerta("orlando"))
print(clientvirgen.compro("orlando","cebiche"))
# objeto 2
clientjona=Mercado("la gringa","femeninio","rosa","venta de celulares","S23 Ultra")
print(clientjona.tipo_de_puesto)
print(clientjona.productos)
print(clientjona.abrir_puerta("jhonatan devorador de mundos"))
print(clientjona.compro("jhonatan","S23 Ultra"))
# objeto 3
clientjona=Mercado("la gringa","femeninio","rosa","venta de celulares","S23 Ultra")
print(clientjona.tipo_de_puesto)
print(clientjona.productos)
print(clientjona.abrir_puerta("jhonatan devorador de mundos"))
print(clientjona.salir("hans"))
# objeto 4
clientchina=Mercado("los facheros","masculino","naranja","venta de ropa","zapatos")
print(clientchina.tipo_de_puesto)
print(clientchina.productos)
print(clientchina.abrir_puerta("jhonatan devorador de mundos"))
print(clientchina.salir("china"))