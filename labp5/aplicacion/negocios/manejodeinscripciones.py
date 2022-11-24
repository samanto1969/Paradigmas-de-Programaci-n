from aplicacion.modelos.usuario import Usuario 
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#========================
# Clase storemanager
# NO TIENE VARIABLES !!!
#=======================

class ManejoDeInscripciones:
    #======================================================================
    # Decorado staticmethod
    # El objeto solo tiene la funcion inscribirUsuario 
    # ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES 
    # el objeo ManejoDeInscripciones contiene la interface  intercambiable 
    #======================================================================

    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("-------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
