class User():
    
    def __init__(self, id = None, nombre = None, apellido = None, sexo = None, dni = None, fecha_nac = None, firma = None, imagen = None, publica = False, edad = None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._dni = dni
        self._fecha_nac = fecha_nac
        self._firma = firma
        self._imagen = imagen
        self._es_publica = publica
        self._edad = edad

class Ingreso():

    def __init__(self, id = None, fecha = None, id_user = None, valido = None):
        self._id = id
        self._fecha = fecha
        self._id_user = id_user
        self._valido = valido


