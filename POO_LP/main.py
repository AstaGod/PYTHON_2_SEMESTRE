from bd import *

class Tiendas_comerciales:

    def tienda_gerente(self,bd_negocios,nombre_gerente):
        respuesta=list(filter(lambda el:el["gerente"]==nombre_gerente,bd_negocios))
        return respuesta

    def tiendas_mas_categorias(self,bd_negocios):
        respuesta1=list(filter(lambda xd:len(xd["categoria"])>2,bd_negocios))
        return respuesta1
    
    def ruc_nombre(self,bd_negocios):
        respuesta2=list(map(lambda par:{"ruc":par["ruc"],"nombre" :par["nombre"]},bd_negocios))
        return respuesta2
    
    def eliminar_negocio(self,bd_negocios,ruc):
        respuesta=list(filter(lambda el:el["ruc"]!=ruc,bd_negocios))
        return respuesta

    ## tarea
    def actualizar_todo(self):
        pass

    ## otro metodo para crear un nuevo producto

    ## otro metodo para actualizar el horario de atencion


gerente=Tiendas_comerciales()
print(gerente.tienda_gerente(negocios,"china"))

categorias=Tiendas_comerciales()
print(categorias.tiendas_mas_categorias(negocios))

ruc_nomb=Tiendas_comerciales()
print(ruc_nomb.ruc_nombre(negocios))

elim=Tiendas_comerciales()
print(elim.eliminar_negocio(negocios,857496321))