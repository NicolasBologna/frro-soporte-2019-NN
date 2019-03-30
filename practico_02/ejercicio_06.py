# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import datetime, date

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.fecha_nac = datetime.strptime(nacimiento, '%m/%d/%y')

    def edad(self):
        return (datetime.now().year - self.fecha_nac.year)


per = Persona('10/15/96')

assert(per.edad()) == 23
