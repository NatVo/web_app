import cv2
import dlib

import numpy as np

class FaceRec():

    def __init__(self):
        pass


    def crop_face(self, img):
        
        #model = '/home/nat/Documents/model/mmod_human_face_detector.dat'
        CNN_FACE_DETECTOR = dlib.get_frontal_face_detector()
        
        dets =  CNN_FACE_DETECTOR(img, 1)
        for i, d in enumerate(dets):
           print(d.left(), d.top(), d.right(), d.bottom())

        try:
            return img[d.top():d.bottom(), d.left():d.right()]
        except:
            pass
    
    def dlib_to_np(self, vect):

        np_array = []

        for i in vect:
            np_array.append(i)

        return np.asarray(np_array, dtype = 'float32')



    def get_img_vector(self, img):
        
        shape_model = '/home/nat/Documents/model/shape_predictor_5_face_landmarks.dat'
        face_rec_model = '/home/nat/Documents/model/dlib_face_recognition_resnet_model_v1.dat'
        #detect_model = '/home/nat/Documents/model/mmod_human_face_detector.dat'
        
        sp = dlib.shape_predictor(shape_model)
        facerec = dlib.face_recognition_model_v1(face_rec_model)
        #face_detector = dlib.cnn_face_detection_model_v1(detect_model)
        face_detector = dlib.get_frontal_face_detector()


        dets = face_detector(img, 1)
        for i, d in enumerate(dets):
           print(d.left(), d.top(), d.right(), d.bottom())
           
        try:
            shape = sp(img, d)
            return facerec.compute_face_descriptor(img, shape)
        except:
            return False


    def compare_img(self, img, img_db):

        img_vect = self.get_img_vector(img)
        img_db_vect = self.get_img_vector(img_db)
        
        #print(img_vect)
        #print(type(img_vect))

        if (img_vect and img_db_vect):
            img_vect = self.dlib_to_np(img_vect)
            img_db_vect = self.dlib_to_np(img_db_vect)
 
            dist = np.linalg.norm(img_vect - img_db_vect)
            print('dist: {}'.format(abs(dist)))

            return abs(dist)
        else:

            return 1
   


        
