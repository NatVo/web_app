import cv2
import base64

import numpy as np

class Img():

    def __init__(self):
        pass

    def decode_img(self, image_b64):
        body = base64.b64decode(image_b64)
        nparr = np.fromstring(body, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        return img

        #self.show_img(img)

    def save_img(self, img, img_path = './img_buffer/tmp.png'):
        cv2.imwrite(img_path, img)


    def show_img(self, img):

        while(1):
            cv2.imshow('img', img)
            if cv2.waitKey(20) & 0xFF == 27:
                break           

        
