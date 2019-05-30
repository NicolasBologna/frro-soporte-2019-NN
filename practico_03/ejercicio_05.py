# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from practico_03.ejercicio_01 import engine, Persona, reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from sqlalchemy.orm import sessionmaker



def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()
    try:
        # work with sess
        per = session.query(Persona).filter(Persona.IdPersona == id_persona).first()

        if per != None:
            session.query(Persona).filter(Persona.IdPersona == id_persona).update({"Nombre": nombre,"FechaNacimiento":nacimiento, "DNI" : dni ,"Altura" : altura})

            session.commit()

            rta = True
        else:
            rta = False
    except:
        session.rollback()
        rta = False
    finally:
        session.close()
        return rta


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
