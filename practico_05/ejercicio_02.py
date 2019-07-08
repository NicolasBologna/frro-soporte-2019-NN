# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio
from pprint import pprint


class DatosSocio(object):

    def __init__(self):

        engine = create_engine('sqlite:///socios.db')
        Base.metadata.drop_all(engine)
        Socio.__table__.create(bind = engine)
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id_socio):
        """Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio"""
        try:
            persona = self.session.query(Socio).filter(Socio.id_socio==id_socio).first()
            rta = persona
        except:
            rta = False

        self.session.close()



        return rta

    def buscar_dni(self, dni_socio):
        try:
            persona = self.session.query(Socio).filter(Socio.dni==dni_socio).first()
            rta = persona
        except:
            rta = False

        self.session.close()
        return rta

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        try:
            personas = self.session.query(Socio).all()
            rta = personas
        except:
            rta = False

        self.session.close()


        return rta

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            socios = self.session.query(Socio).all()
            for socio in socios:
                self.session.delete(socio)
            self.session.commit()
            rta = True
        except:
            rta = False

        return rta


    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()


        return socio

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            persona = self.session.query(Socio).filter(Socio.id_socio==id_socio).first()

            self.session.delete(persona)
            self.session.commit()

            rta = True
        except:
            self.session.rollback()
            rta = False
        finally:
            self.session.close()


        return rta

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        '''self.session.query(Socio).filter(Socio.id_socio == socio.id_socio).update({Socio.nombre: socio.nombre},{Socio.apellido: socio.apellido}, {Socio.dni: socio.dni})'''
        try:
            orig = self.session.query(Socio).filter(Socio.id_socio == socio.id_socio).first()
            orig.nombre = socio.nombre
            orig.apellido = socio.apellido
            orig.dni = socio.dni
            self.session.commit()
        except:
            self.session.rollback()
        return socio


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id_socio > 0

    # baja
    assert datos.baja(socio.id_socio) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id_socio) == socio_2

    # buscar dni
    #socio_2 = datos.alta(Socio(dni=22345679, nombre='Carla', apellido='Perez'))
    '''pprint(vars(socio_2))
    pprint(vars(datos.buscar_dni(socio_2.dni)))'''

    assert datos.buscar_dni(socio_2.dni).dni == socio_2.dni

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id_socio)
    assert socio_3_modificado.id_socio == socio_3.id_socio
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
