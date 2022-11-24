from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#==============================================================================
# S3 es hijo de RepositorioDeUsuarios
#==============================================================================
class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretKer: str
    __bucket: str


    def __init__(mi, clientId: str, secretKer: str, bucket: str)
    mi.__clientId = clientId
    mi.__secretKey = secretKey
    mi.__bucket = bucket


    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi.__clientId}:{mi.__secretkey}")

