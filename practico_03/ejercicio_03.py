# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from practico_03.ejercicio_02 import agregar_persona

import datetime

from sqlalchemy.orm import sessionmaker

from practico_03.ejercicio_01 import engine, Persona, reset_tabla
from sqlalchemy.ext.declarative import declarative_base


def borrar_persona(id_persona):
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()
    try:
        # work with sess
        persona = session.query(Persona).filter(Persona.IdPersona==id_persona).first()

        session.delete(persona)
        session.commit()

        rta = True
    except:
        session.rollback()
        rta = False
    finally:
        session.close()
    
    return rta


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
