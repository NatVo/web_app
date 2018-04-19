import cv2
import dlib

class FaceRec():

    def __init__(self):
        pass


    def crop_face(self, img):
        
        model = '/home/nat/Documents/mmod_human_face_detector.dat'
        CNN_FACE_DETECTOR = dlib.cnn_face_detection_model_v1(model)
        
        dets =  CNN_FACE_DETECTOR(img, 1)
        for i, d in enumerate(dets):
           print(d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom())

        #img = cv2.rectangle(img, (d.rect.left(), d.rect.top()), (d.rect.right(), d.rect.bottom()), (0,255,0), 1)
        try:
            return img[d.rect.top():d.rect.bottom(), d.rect.left():d.rect.right()]
        except:
            pass
 
