import pickle
from datetime import date

class Utiles():

    @staticmethod
    def deBinario(binario):
        return pickle.loads(binario)

    @staticmethod
    def aBinario(array):
        return Binary(pickle.dumps(array, protocol=2), subtype=128)

    @staticmethod
    def calculaEdad(fecha_nac):
        fnac = fecha_nac.split('/')
        hoy = date.today()
        edad = hoy.year - int(fnac[2]) - ((hoy.month, hoy.day) < (int(fnac[1]), int(fnac[0])))
        return str(edad)