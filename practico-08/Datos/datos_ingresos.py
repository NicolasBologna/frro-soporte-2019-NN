from Datos.datos_connection import Connection

class IngresoData():

    @staticmethod
    def crearIngreso(ingreso):
        db = Connection.connect()
        nuevo = db.ingreso
        nuevo.insert_one(ingreso)

    @staticmethod
    def traerIngresos():
        db = Connection.connect()
        
        lista_final = []

        lista_ingresos = []
        lista_usuarios = []           
        cursor = db.usuario.find({})
        for i in cursor:
            lista_usuarios.append(i)
        cursor = db.ingreso.find({})
        for i in cursor:
            lista_ingresos.append(i)

        for id_ingreso,ingreso in enumerate(lista_ingresos):
            for persona in lista_usuarios:
                if ingreso['id_user'] == persona['_id']:
                    lista_ingresos[id_ingreso]['nombre_apellido'] = persona['nombre']+' '+persona['apellido']
                    lista_ingresos[id_ingreso]['dni'] = persona['dni']
                    lista_final.append(lista_ingresos[id_ingreso])
                    break
        return lista_final

if __name__ == "__main__":
    print(IngresoData.traerIngresos())
