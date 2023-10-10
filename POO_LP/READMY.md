# Proframacion Orientado a Objetos(POO)
### En ingles es Object Orient Programing(OOP)
es un paradigma de programacion
> **Paradigma** - es un modelo, patron o ejemplo que se debe seguir

POO es un modelo de como programar
**Objeto** - el objetivo es organizar el codigo de manera que se asemeje a como pensamos en la vida real

se basa en Objetos y en la POO un objeto es toda entidad que se puede describir atravez de
**atributos0** y las **funciones** que puede realizar la entidad

```python
# en nombre siempre debera ser en singular y con la primera letra mayuscula
class Perro:
    nombre="boby"
    edad="2 meses"
    color="cheqche"
    raza="chusterrier"

    def ladrar(self):
        return "gua gua mascota"

    def correr(self.pasos):  # self es para señalar que esta funcion pertenece al objeto
        response=f"corriste {pasos}, pasos"
        return huevo

respuesta=Perro()
print(respuesta.nombre)
print(respuesta.ladrar())
print(respuesta.correr(10))
```

```python
class Celular:
    # atributos de tipo clase
    # que son inguales para todos los objetos
    # que se creen
    familia="smart phone"

    # atributos de instancia
    # son atributos propios del objeto
    # creamos una funcion inicializadora
    def __init__(self,marca,modelo,imei,nroCelular):
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.nroCelular=nroCelular


    # funcionalidades
    def llamar(self,destino):
        return f"llamando a {destino}"

# objeto celular jory
llamandoJory=Celular("poco","x5","46464664","948456786") #  instaciando mi clase . creador mi objeto celular

print(llamandoJory.marca)
print(llamandoJory.familia)
print(llamandoJory.llamar("China"))

# objeto celular nadine
llamandoNadine=Celular("alcatel","basico","6545648613","946543812")
print(llamandoNadine.marca)
print(llamandoNadine.familia)
print(llamandoNadine.llamar("Jhonatan"))
```