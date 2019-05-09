# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, INT

from sqlalchemy import create_engine

import sqlite3


engine = create_engine('sqlite:///sqlalchemy_ejemplo.db', echo=True)

Base = declarative_base()

def crear_tabla():

    class Persona(Base):
        __tablename__ = 'persona'
        IdPersona = Column(Integer, primary_key=True)
        Nombre = Column(String)
        FechaNacimiento =  Column(Date)
        DNI = Column(INT)
        Altura = Column(INT)

    Base.metadata.create_all(engine)


def borrar_tabla():
    print(Base.metadata)
    Base.persona.drop(engine)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

crear_tabla()
#borrar_tabla()
