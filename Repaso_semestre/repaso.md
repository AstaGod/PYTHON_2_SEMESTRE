# REPASO PYTHON
## 1. TIPOS DE DATOS :
### DATOS PRIMITIVOS:
#### string :
'a'-> string cadena texto

'hola'-> es tambien un string

'hola soy string'-> cadena larga

**observacion** : todo lo que esta en comillas dobles o simples es un string
- '100'
- 'False'
- "Hola"
#### numerico :
- 100-> este es un tipo de dato numerico entero
- 2.1-> este es un tipo de de dato numerico flotante float
#### boleano :
- False -> este es un tipo de dato boleano faso
- True -> este es un tipo de dato boleano verdadero
## 2. VARIABLES
es donde almacenamos uestro tipo  es **=**e datos, pero esos datos pueden cambiar o modificarse.

**como crear una variable**:
1. Darle un nombre significativo o relacionado al dato que vamos a almacenar.
2. Indicarle a que dato esta relacionado-> *asignación* es **=**
3. indicar el tipo de dato que va almacenar-> darle el dato a guardar

edad_alumno = 18
## 3. OPERADORES
### 1. operadores aritmeticos
#### suma :
- suma = 45+2
#### resta :
- resta = 30-20
#### multiplicacion : 
- multiplicacion= 10*2
#### divicion :
- divicion= 10/2
##### precedencia e operadores
### operadores de uso especial
- suma = 45+42 **el resultado sera 87**
- suma ='45' + 12 resulta **4512**
- saludo= 'hola'+'mundo'-> concatenacion **holamundo**
- saludo= 'hola' + 'mundo'-> concatenacion **hola mundo**
- saludo= ' hola'*2 -> **holahola**
## 4. DATOS ESTROCTURADOS:
son tipos de datos que ya tienen estrocturas de alguna manera
existen dos

### listas :
puede almacenar distintos tipos de datos en una sola lista

lista = ['nombre',10,false]
alumnos =[]
### objeto :
tambien al igual que las lista amacenan distintos tipos de dato pero con un orden para almacenar datos en un objetos nececitamos especificar un indice y un valor a esto se le conoce como clave->valor
alumno ={
'nombre' : 'jhonatan',
'edad' : '19',
'sexo' : 'todos los dias'
'amigos': 'hans' , 'cristhian','nadine','edwin'
}
ALUMNOS=[{},{},{}]
## 5. CONTROLES DE FLUJO :
SOLO EXISTEN 2 
### DECICIONES:

SOLOLO SE EJECUTA EL CODIGO SI LA CONDICION ES VERDERA PODEMOS HACER QUE SI LA COONDICION SEA FALSA SE EJECUTE ORO CODIGO
SINTAXIS : PRIMERO ESPECIFICAR EL CODIGO  QUE SE EJECUTARA SI CUMPLE UNA CONDICION
```PYTHON
if <condicion>:
    ##el codigo que deseamos ejecutar si la condicion es verdad 
    print('ejecuta esto')
    ##aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if 
```
```python
# si queremos que se ejecute un codigo en caso que sea falso 
if <condicion falsa>:
    print('solo imprime si es verdad')
else:
    print('solo imprime si es falso')
```
```python
#ejemplo
if 15 > 18:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
```
```python
if 15*2 ==30:
    print('si es verdad imprime esto')
else:
    print('si es falso imprime esto')
```
### CICLOS: 
existen 2 tipos
#### iterar cuando sabes la cantidad de veces que vamos a repetir
para este caso esxiste for 

sintaxis despues de la palabra reservada for deberemos crear una variable de almacene el numero que iremos luego tendremos que indicar el rango a itera los elementos a iterar
```python
vocales= ['a','e','i','o','u']
for i in vocales:
    print(i)
```  
#### cuando no sabemos la cantidad de veces de repiter 
```python
condicion=True
while condicion:
    print("hola")
    texto=inmput("ingresa tu nombre o salir para terminar el programa")
    if texto="salir":
        condicion=False
```

## 6. FUNCIONES :
Existen 2 tipos de funciones
### 1. propias del lenguaje
que ya bienen creadas e insertadass en python y estan listas para ser usadas
### estructura de uso de una funcion
tiene el nombre seguido de parentesis,
dentro de la parentesis podremos pasarles datos que necesita la funcion para ejecutarse
### Esta es una funcion que nos sirve par mostrar por consola datos
```python
print("hola")
```
### len nos devuelve un numero
```python
print(len([1,5,6,7,8]))
```
### esta es una funcion que se detiene a esperar al usuario introdusca informacion
### entre parentesis podremos escribir un mensaje que indique que accion realizara el usuario
```python
input("ingresa algo: ")
```
### esta funcion nos muestra el numero mayor de una lista
```python
lista=[45,12,78,3,24,50]
numero_mayor=max(lista)
print(numero_mayor)
```
### esta funcion nos muestra el numero menor de una lista
```python
lista=[45,12,78,9,6,12]
numero_menor=min(lista)
print(numero_menor)
```
### funcion para convertir de un string a un numero entero
```python
numero_string="100"
print(type(numero_string))
numero_entero=int(numero_string)
print(type(numero_entero))
```
### funcion para convertir un entero a un string
```python
str(100) # ->> 100 ->> string
```
### funcion de python que nos permite agregar elementos al final de una lista
```python
lista=[15,72,78]
elemento=100
lista.append(elemento)
print(lista)
```
### funcion de python que nos permit eliminar los elementos que se encuentran al final de una lista
```python
lista=[15,12,78] # pop elimina el ultimo elemento de la lista y lo guarde el elemnto en una variable si esque se desesa
lista.pop()
print(lista)
```
### funcion de python que nos permite agregar elementos en cualquier posicion de mi lista para eso se le tiene que pasar dos parametros, primero indicarle el indice y segundo el dato que e va agregar
```python
lista_nombres=["jory","nadine","bichota"]
lista_nombres.insert(1,"satan")
print(lista-nombres)
```
### funcion de python que nos permite eliminar elementos de cualquier posicion de una lista, esta funcion recibe solo el elemento que deseamos eliminar
```python
lista=[4,5,6,8,7]
lista.remove(6)
print(lista)
```
### funcion que nos permite dividir en una lista una cadena
```python
cadena="hola como estan"
lista=cadena.split()
print(lista)
url="www.golle.com/id=70133573"
id=url.split("=").pop()
print(id)
```
### 2. funciones propias
#### Una funcion son mini programas, tambien se le conoce como modulos o fragmentos de codigo de uso exclusivo
### pasos para crear una fruncion propia
#### 1. hacer uso de la palabra reservada def
#### 2. definir un nombre de funcion que describa que tarea va a realizar
#### 3. establecer los param,etros que resivira la funcion entre parentesis ()
#### 4. establecer que valor o dato va retornar mi funcion con la palabra reservada "return"
#### observacion =>> tambien podemos hacer uso de la funcion print() para retornar un mensaje en nuestra funcion
#### existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros
### funcion sin parametros
```python
def saludo():
    print("hola este es un saludo")
# como hacemos uso de la funcion??
# nombre de la funcion y parentesis
saludo()
```
### funcion con parametros
```python
def mi_print(texto):
    print(texto)

print("hola este es print de python")
mi_print("hola este es mi print creado")
```
```python
def suma(a,b):
    total=a+b
    return total

mi_print(suma(45,12)) ##=> 57
```
### ejemplo
```python
lista=[12,4,45,78,3,1]
mi_print(max(lista)) # =>78

def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
    return numero_mayor
mi_print(mi_max(lista))
```
```python
lista=[12,4,45,78,3,1]
mi_print(min(lista)) # =>78

def mi_min(lista):
    numero_menor=lista[0]
    for numero in lista:
        if numero < numero_menor:
            numero_menor=numero
    return numero_menor
mi_print(mi_min(lista))
```
### funciones con muchos parametros
```python
def funcion(*muchos_parametros):    # el * es para poner varios parametros
    total=0
    for numero in muchos_parametros:
        total=total+numero
    return total

print(funcion(45,78,45,415))
```
```python
def datos(*args):
    nombre=args[0]
    apellido=args[1]
    edad=args[2]
    return f"mi nombre es,{nombre},{apellido} y mi edad es {edad}"

print(datos("edwin","lopez","19"))