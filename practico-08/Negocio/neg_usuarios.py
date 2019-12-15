from Datos.datos_usuarios import UsuarioData
from bson.binary import Binary
import pickle, os, cv2
import face_recognition
import glob
from bson.objectid import ObjectId

import inspect
from subprocess import call

from Otros.Entidades import User
from Otros.utiles import Utiles

class Users():
    
    @staticmethod
    def saveUser(datos_persona_dni, imagen):
        'parametros(datos_persona_dni,cara_reconocida,imagen)'
        datos_separados = datos_persona_dni.split('@')
        cara_reconocida = face_recognition.face_encodings(imagen)
        a = {'nombre': datos_separados[2], 'apellido': datos_separados[1], 'sexo' : datos_separados[3], 'dni' : datos_separados[4], 'fecha_nac' : datos_separados[6] ,'firma': Binary(pickle.dumps(cara_reconocida, protocol=2), subtype=128), 'imagen' : Binary(pickle.dumps(imagen, protocol=2), subtype=128), 'publica' : False}
        usuario_dict = UsuarioData.crearUsuario(a)

        img = Binary(pickle.dumps(imagen, protocol=2), subtype=128)
        img = pickle.loads(img)

        usr = User(usuario_dict['_id'],usuario_dict['nombre'],usuario_dict['apellido'],usuario_dict['sexo'], usuario_dict['dni'], usuario_dict['fecha_nac'], cara_reconocida, img ,usuario_dict['publica'],Utiles.calculaEdad(usuario_dict['fecha_nac']))
        return usr

    @staticmethod
    def cargarImagenes():
        'En desuso'
        contador = 0

        listadoImagenes = glob.glob("img\\*.*")
        known_face_encodings = []
        known_face_names = []
        for i in listadoImagenes:
            contador += 1
            imagen = face_recognition.load_image_file(str(i))  # Carga la imagen como numpy.array
            try:
                cara_reconocida = [face_recognition.face_encodings(imagen)[0]] # Devuelve la firma facial
                known_face_encodings = known_face_encodings + cara_reconocida  # Agrega la nueva firma digital
                known_face_names = known_face_names+[os.path.splitext(os.path.basename(str(i)))[0]]
                a = {'nombre': os.path.splitext(os.path.basename(str(i)))[0], 'apellido': '',
                        'firma': Binary(pickle.dumps(cara_reconocida, protocol=2), subtype=128), 'imagen' : Binary(pickle.dumps(imagen, protocol=2), subtype=128)}
                UsuarioData.crearUsuario(a)
                print(contador, ' imagen cargada')
                exito = True
            except:
                exito = False
                pass
        if exito:        
            print('de las: ',len(listadoImagenes),' imágenes, se cargaron: ', len(known_face_encodings))
        else:
            print('Error en la carga.')
        return known_face_encodings, known_face_names
    
    
    @staticmethod
    def cargarTodos():
        'trae todos los usuarios de la base, nombre y firma digital'
        known_face_names = []
        known_face_encodings = []
        usuarios = []
        lista_usuarios = []
                        
        cursor = UsuarioData.traerUsuarios()
        for i in cursor:
            lista_usuarios.append(i)
        cursor = ''
        try:
            for i in lista_usuarios:
                firma = pickle.loads(i["firma"])
                i.update((k, firma) for k, v in i.items() if k == "firma")
                imagen = pickle.loads(i["imagen"])
                i.update((k, imagen) for k, v in i.items() if k == "imagen")
            for usuario_dict in lista_usuarios:
                usr = User(usuario_dict['_id'],usuario_dict['nombre'],usuario_dict['apellido'],usuario_dict['sexo'], usuario_dict['dni'], usuario_dict['fecha_nac'], usuario_dict['firma'],usuario_dict['imagen'],usuario_dict['publica'], Utiles.calculaEdad(usuario_dict['fecha_nac']) )
                usuarios.append(usr)
                known_face_encodings.append(usuario_dict["firma"][0])
        except:
            print('no hay gente cargada')
        return known_face_encodings, usuarios

    @staticmethod
    def borrarTodos():
        UsuarioData.borrarTodos()

    @staticmethod
    def leerDni(img_dni):
        #cv2.imwrite("C:\\Users\\Matias\\Desktop\\Facultad\\Soporte\\TP integrador\\Soporte\\ReadBarcode\\img_dni.jpg" , img_dni)
 
        #return os.popen("C:\\Users\\Matias\\source\\repos\\BarcodeReadDemo_CPP\\x64\\Debug\\BarcodeReadDemo_CPP.exe").read()
        cv2.imwrite("ReadBarcode/img_dni.jpg" , img_dni)
        return os.popen('ReadBarcode/./ReadBarcode ReadBarcode/img_dni.jpg').read()


    def getById(self, IdUser):
        datos_user = UsuarioData.buscar_por_id(IdUser)
        firma = Utiles.deBinario(datos_user['firma'])
        imagen = Utiles.deBinario(datos_user['imagen'])
        user = User(datos_user['_id'],datos_user['nombre'],datos_user['apellido'],datos_user['sexo'],datos_user['dni'], datos_user['fecha_nac'], firma, imagen )
        return user

        
if __name__ == '__main__':
    user = Users()
    print(inspect.getmembers(user.getById(ObjectId("5d3c99ccafff5e4395a23281"))))
