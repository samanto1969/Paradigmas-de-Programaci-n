from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#=========================================================
# Clase storemanager
# NO TIENE VARIABLES !!!
#=========================================================
class ManejoDeInscripciones:
    #=====================================================
    # Decorador staticmenthod
    # El objeto sólo  tiene la función inscribirUsuario
    # ENVIELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    # ======================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()


