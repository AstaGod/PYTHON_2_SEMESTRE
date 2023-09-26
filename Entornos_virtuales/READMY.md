# ENTORNOS VIRTUALES
poetry
virtualeny
venv -> manejador de entorno virtuales ya preinstalado en python
conda

pip -> es un comando que nos permite instalar paquetes de python en nuestros proyectos

pipenv -> creador de entronos virtuales desfasado (ya no se usa)
pyenv -> manejador de versiones de python

# Para crear un entorno virtual

1. nos ubicamos en la carpeta que deseamos crear el entorno virtual "bash"
cd <"ruta del archibo">

Ejemplo
cd nombre_carpeta/entorno_uno

2. creamos el entorno virtual con el siguiente comando
```python
python -m venv <nombre de nuestro entorno virtual>
#ejemplo
python -m venv mi_entorno
```

3. Para activarel entorno virtual con el gitbash como terminal predeterminado corremos, el siguiente comando solo para windouws
```python
source venv/Scripts/activate
```
### OBSERVACIONES
1. para poder ejecutarlo en powershell como terminal precdeterminado ejecutar el siguiente comando
```python
venv\Scripts\Activate.ps1
```

# Para instalar paquetes en nuestro entorno virtual
1. primero verificamos que no tengamos el paquete instaqlado y lo listamos con el siguiente comando

debemos tener activado nuestro entorno virtual primero
```python
pip list
```
2. luego intalaremos con el siguiente comando
```python
pip install <nombre del paquete>
#ejemplo
pip install pandas
```
# Crear un entorno virtual con venv de python e instalar el framework django para la creacion de app web

## crear entorno
## activar entorno
## instalar elm  entorno