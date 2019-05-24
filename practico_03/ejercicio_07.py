# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla, PersonaPeso
from practico_03.ejercicio_04 import buscar_persona

engine = create_engine('sqlite:///sqlalchemy_ejemplo.db', echo=False) #cambiar a True para ver el log


def agregar_peso(id_persona, fecha, peso):
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    if buscar_persona(id_persona) != False:
        # work with sess

        personasPesos = session.query(func.max(PersonaPeso)).filter(PersonaPeso.persona == id_persona).all()
        print(personasPesos)

        persona =  Persona(Nombre=nombre, FechaNacimiento=nacimiento,DNI=dni,Altura=altura)
        session.add(persona)
        session.commit()
        session.refresh(persona)
        id = persona.IdPersona
        return id


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
