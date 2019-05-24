# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, table, DateTime, INT, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla, Persona

engine = create_engine('sqlite:///sqlalchemy_ejemplo.db', echo=True) #cambiar a True para ver el log

Base = declarative_base()

class PersonaPeso(Base):
    __tablename__ = 'personaPeso'
    IdPersona = Column(Integer, ForeignKey('persona.IdPersona'), primary_key=True)
    Fecha =  Column(DateTime)
    Peso = Column(INT)

def crear_tabla_peso():

    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()
    persona = session.query(Persona).first()
    print(persona)
    print('asdsadad')
    PersonaPeso.__table__.create(bind = engine)

def borrar_tabla_peso():
    Base.metadata.drop_all(engine)

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
