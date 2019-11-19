# Buscar --rev para ir comentando lo que no se que hace

import face_recognition
import cv2
import numpy as np
import glob
import os
import sys
import time
from bson.binary import Binary
import pickle
import datetime
import requests
import time


from Otros.utiles import Utiles

from Negocio.neg_usuarios import Users
from Negocio.neg_ingresos import Ingresos

from Interfaz.UI_msg_dni import mostrar_msg_dni


class Reconocimiento():

    def __init__(self):
        self.known_face_encodings = []
        self.known_face_encodings, self.usuarios = Users.cargarTodos()
        #si alta es true busca dni y no rostros
        self.alta = False

        #seteos para save con click
        self.ix,self.iy = -1,-1
        self.contador_circulo_click = 0
        self.color_circulo_click = ''

        ############ ---INICIALIZACIONES-- ############

        #inicializo la lista de fotos con el nombre de cada persona encontrada
        self.fotos_anteriores = []
        self.fotos_desconocidos = []
        self.face_locations = []
        self.face_encodings = []

        # Configuraciones iniciales
        self.cant_frames_saltados = 10
    
    # Función que guarda la cara con un click

    def save_face_click(self,event,x,y,flags,param):
        
        if event == cv2.EVENT_LBUTTONDOWN: 
            self.ix,self.iy = x,y
            self.contador_circulo_click = 5
            self.color_circulo_click = (0,0,255)
            for foto_desconocido in self.fotos_desconocidos:
                if self.ix >= foto_desconocido[1]['left'] and self.ix <= foto_desconocido[1]['right'] \
                    and self.iy >= foto_desconocido[1]['top'] and self.iy <= foto_desconocido[1]['bottom']:
                    self.imagen = foto_desconocido[0]
                    imagen_mostrar = self.imagen

                    imagen_mostrar = Binary(pickle.dumps(imagen_mostrar, protocol=2), subtype=128)
                    imagen_mostrar = pickle.loads(imagen_mostrar)
                    
                    mostrar_msg_dni(self,imagen_mostrar)
                    
                    color_circulo_click = (0,255,0)
                    (video_x, video_y, video_w, video_h) = cv2.getWindowImageRect('Video')
                    self.alta = True

                    #descomentar si queres cambiar de camara para leer el dni
                    #self.video_capture = cv2.VideoCapture(2)

    ##############################################################################################################################################
    def reconocer(self):
        ############ ---CONFIGURACIONES-- ############

        # Get a reference to webcam #0 0 es la cámara de la note, 2 es la camara USB en mi caso.
        self.video_capture = cv2.VideoCapture(0)
        #url="http://192.168.0.95:8080/photoaf.jpg"

        #Fuente para las letras de los recuadros
        font = cv2.FONT_HERSHEY_DUPLEX 

        #contador para saltar frames de busqueda de rostro
        contador_busca_rostro = 0

        while True:
            
            self.fotos_desconocidos = [] 

            ret, frame = self.video_capture.read()

            if frame is not None:

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_frame = frame[:, :, ::-1]
                
                if self.alta:
                    datos_persona_dni = Users.leerDni(frame)
                
                    #cv2.putText(frame, 'ACERQUE EL CODIGO DE BARRAS DEL DNI A LA CAMARA', (20, 20), font, 0.6, (0, 255, 100), 1)
                    #uso el @ in para evitar falsos positivos
                    if '@' in datos_persona_dni:
                        usuario = Users.saveUser(datos_persona_dni, self.imagen)
                        self.usuarios.append(usuario)
                        self.alta = False
                        self.known_face_encodings = self.known_face_encodings + usuario._firma

                else:

                    if contador_busca_rostro == 0:
                        self.face_locations = face_recognition.face_locations(rgb_frame, 0)
                        self.face_encodings = face_recognition.face_encodings(rgb_frame, self.face_locations)

                    # Recorre cada cara de la imagen
                    for (top, right, bottom, left), face_encoding in zip(self.face_locations, self.face_encodings):

                        #top, right, bottom, left vienen del face location de cada cara

                        # See if the face is a match for the known face(s)
                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.6)

                        # Draw a label with a name below the face
                        cv2.rectangle(frame, (left-15, top - 35), (right+15, top-15), (255, 0, 0), cv2.FILLED)

                        # If a match was found in known_face_encodings, just use the first one.
                        if True in matches:
                            first_match_index = matches.index(True)
                            user = self.usuarios[first_match_index] #asigna a usuario el nombre del archivo de la imagen con la que coinicidió   
                        
                            ingreso_ok = Ingresos.puedeIngresar(user._edad)                
                            
                            Ingresos.saveIngreso(user._id,user._edad)       

                            self.video_capture.release()
                            cv2.destroyAllWindows()
                            return (user, ingreso_ok )


                        else:
                            self.fotos_desconocidos.append([frame[top-15:bottom+15, left-15:right+15],{"top": top-15,"bottom": bottom+15,"left":left-15,"right":right+15}]) #agrego la foto de de la cara a un arreglo de caras encontradas desconocidas
                            cv2.putText(frame, "Desconocida/o", (left + 6, top - 21), font, 0.5, (104, 197, 219), 1)
                            cv2.putText(frame, "DEBE REGISTRARSE", (left, bottom + 30), font, 0.6, (250, 250, 250), 1)
                            cv2.putText(frame, "HAGA CLICK EN SU ROSTRO", (left , bottom + 50), font, 0.6, (0, 0, 0), 1)
                            color_recuadro = (0, 0, 255)

                        # Draw a box around the face
                        cv2.rectangle(frame, (left-15, top-15), (right+15, bottom+15), color_recuadro, 2)
                
                    if contador_busca_rostro == self.cant_frames_saltados:
                        contador_busca_rostro = 0
                    else:
                        contador_busca_rostro += 1  

                cv2.imshow('Video', frame)

                #Funcion para guardar la cara con un click
                cv2.setMouseCallback('Video',self.save_face_click)     

                k = cv2.waitKey(1)
                        
                if k== ord('q'):
                    self.video_capture.release()
                    cv2.destroyAllWindows()
                    return (1,0)
                    break
                elif k == ord('d'):
                    self.alta = True
                elif k == ord('c'):
                    # Hago la carga desde la carpeta imágenes
                    self.known_face_encodings, known_face_names = Users.cargarImagenes() # Traigo todas las firmas y nombres
                
                    print('Personas cargadas con imágenes:')
                    print(known_face_names)
                elif k == ord('b'):
                    #self.usuarios = []
                    Users.borrarTodos()
                    self.known_face_encodings = []

        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()
        return 0


####################################################################################################################################################

if __name__ == "__main__":
    principal1()


