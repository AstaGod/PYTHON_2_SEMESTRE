# lambda un funcio que se autoejecuta
hola=lambda a,b:print(a+b)
# funcion normal
def suma(a,b):
    print(a+b)
suma(4,6)
hola(10,20)

# if ternario
ternario="soy verdad ternario" if True else "soy falso ternario"
print(ternario)
# if normal
if True:
    print("soy verdad")
else:
    print("soy mentira")

lista_alumnos=[
    {
        "nombre":"edwin",
        "edad":15,
        "hobby":"danza",
        "flaquita":"melody"
    },
    {
        "nombre":"del mar",
        "edad":30,
        "hobby":"rodar",
        "flaquita":"melody"
    },
    {
        "nombre":"orlando",
        "edad":14,
        "hobby":"ponchar",
        "flaquita":"sami"
    },
    {
        "nombre":"jory",
        "edad":50,
        "hobby":"danza",
        "flaquita":"xd"
    },
    {
        "nombre":"hans",
        "edad":12,
        "hobby":"quemarse",
        "flaquita":"hermana"
    }
]

print(f"todos mis alumnitos{lista_alumnos}")
fans_melody=list(filter(lambda par:par["flaquita"]=="melody",lista_alumnos))
print(f"los que quieren con melody {fans_melody}")

nuevo_objet=list(map(lambda par:{"nombre_alumno":par["nombre"],"germita" :par["flaquita"]},lista_alumnos))
print(nuevo_objet)

## Tarea
#### 1. crear una lista con 10 objetos que contengan los datos de la tiendas comerciales
#-> ejemplo:

tiendas=[
    {
        "ruc":465463213456,
        "nombre":"el pichilon",
        "categoria":["abarrotes"],
        "horario_atencion":{
            "dia":"7am-12pm",
            "tarde":"2pm-8pm"
        }
        "gerente":"nadine"
    }
]

# observacion : las categorias sera 4: abarrotes, farmacia, bodega, restaurant
# observacion : los gerentes solo podran ser los siguientes: edwin,china,crhistian,nadine
# realizar los siguientes ejercicios
## crear una clase para tiendas qwue tenga los siguientes metodos o casos de uso.
# 1. crear un metodo que me filtre las tiendas que tiene cada gerente
# 2. crear un metodo que me muestre lso negocios que tienen mas de dos categorias
# 3. crear un metodo que me muestre solo el nombre y ruc de la tienda