# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date,DateTime, INT, MetaData
from sqlalchemy import create_engine

import sqlite3

from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///sqlalchemy_ejemplo.db', echo=False) #cambiar a True para ver el log

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'persona'
    IdPersona = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String)
    FechaNacimiento =  Column(DateTime)
    DNI = Column(INT)
    Altura = Column(INT)


def crear_tabla():
    Persona.__table__.create(bind = engine)

def borrar_tabla():
    Base.metadata.drop_all(engine)

def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

borrar_tabla()
