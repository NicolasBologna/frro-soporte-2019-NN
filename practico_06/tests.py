# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)


    def test_regla_1(self):
        # pre-condiciones: 1 socio registrado con dni 12345678
        socio_noexitente = Socio(dni=33333333, nombre='Nicolas' , apellido = 'Bologna')
        unico = self.ns.regla_1(socio_noexitente)
        self.assertTrue(unico)

        repetido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(repetido)
        self.assertRaises(DniRepetido, self.ns.regla_1, repetido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Nombre_de_prueba_de_mas_de_15_caracteres', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Apellido_de_prueba_de_mas_de_15_caracteres')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):

        for i in range(201):
            user = Socio(dni=i, nombre='Juan', apellido='Perez')
            self.ns.alta(user)

        user_excedido = Socio(dni=333, nombre='Juan', apellido='Perez')
        #self.assertRaises(MaximoAlcanzado, self.ns.alta(user_excedido)) Tengo dudas con esta línea

    def test_baja(self):

        user = Socio(dni=777, nombre='Juan', apellido='Perez')
        self.ns.alta(user)

        self.assertTrue(self.ns.baja(user.id_socio))
        self.assertFalse(self.ns.baja('423'))


    def test_buscar(self):

        user = Socio(dni=777, nombre='Juan', apellido='Perez')
        self.ns.alta(user)

        self.assertIsNotNone(self.ns.buscar(user.id_socio))
        self.assertIsNone(self.ns.buscar(12144))

    def test_buscar_dni(self):

        user = Socio(dni=777, nombre='Juan', apellido='Perez')
        self.ns.alta(user)

        self.assertIsNotNone(self.ns.buscar_dni(user.dni))
        self.assertIsNone(self.ns.buscar_dni(12144))

    def test_todos(self):

        #Pre-condición: hay 5 cargados
        for i in range(5):
            user = Socio(dni=i, nombre='Juan', apellido='Perez')
            self.ns.alta(user)

        self.assertEqual(len(self.ns.todos()), 5)


    def test_modificacion(self):
        # pre-condiciones: 1 socio registrado con dni 777 y apellido Perez
        user = Socio(dni=777, nombre='Juan', apellido='Perez')
        self.ns.alta(user)

        # ejecuto la logica
        user.apellido = 'Ramirez'
        self.ns.modificacion(user)

        #post-condiciones: el socio modificado con apellido Ramirez
        socio_modificado = self.ns.buscar_dni(777)
        self.assertEqual(socio_modificado.apellido, 'Ramirez')
