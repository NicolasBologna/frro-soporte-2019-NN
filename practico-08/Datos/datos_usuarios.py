from Datos.datos_connection import Connection


class UsuarioData():

    @staticmethod
    def crearUsuario(usuario):
        db = Connection.connect()
        nuevo = db.usuario
        _id = nuevo.insert_one(usuario)
        return UsuarioData.buscar_por_id(_id.inserted_id)

        
    @staticmethod
    def traerUsuarios():
        db = Connection.connect()
        lista = db.usuario.find({})
        return lista

    @staticmethod
    def borrarTodos():
        db = Connection.connect()
        db.usuario.remove()

    @staticmethod
    def buscar_por_id(userid):
        db = Connection.connect()
        return db.usuario.find_one({"_id": userid})

if __name__ == '__main__':

    from Entidades import User
    user = {'nombre' : 'asdad', 'apellido' : 'dasdsa'}
    sadas = UsuarioData.crearUsuario(user)
    print(sadas)
