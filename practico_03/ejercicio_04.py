# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
from pprint import pprint

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from sqlalchemy.orm import sessionmaker
from practico_03.ejercicio_01 import engine, Persona, reset_tabla


def buscar_persona(id_persona):
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    try:
        # create a Session
        session = Session()
        persona = session.query(Persona).filter(Persona.IdPersona==id_persona).first()
        rta = (persona.IdPersona,persona.Nombre,persona.FechaNacimiento,persona.DNI,persona.Altura)
    except:
        rta = False

    session.close()
    return rta

@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
