from Datos.datos_ingresos import IngresoData

from Otros.utiles import Utiles

from datetime import datetime

edad_minima = 22

class Ingresos():

    
    @staticmethod
    def saveIngreso(id_user,edad):
        if int(edad) >= edad_minima:
            valido = True
        else: 
            valido = False
        a = {'fecha': str(datetime.today()), 'id_user': id_user, 'valido' : valido}
        IngresoData.crearIngreso(a)
    
    @staticmethod
    def puedeIngresar(edad):
        if int(edad) >= edad_minima:
            return True
        else:
            return False

    @staticmethod
    def traerIngresos():
        return IngresoData.traerIngresos()


