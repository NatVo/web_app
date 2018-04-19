import cv2
import numpy as np

from keras import optimizers
from keras.models import load_model



class Predict():
    
    def __init__(self, model_path, img):

        self.model_path = model_path
        self.img = img

        self.loss = 'binary_crossentropy'
        self.optimizer = optimizers.RMSprop(lr = 1e-4)
        self.metrics = ['accuracy']

        self.height = 224
        self.width = 224

    def predict(self):
        
        model = load_model(self.model_path)
        self.img = self.img_prep(self.img)
        print(self.img.shape)

        model.compile(loss = self.loss,
                      optimizer = self.optimizer,
                      metrics = self.metrics)

        prediction = model.predict(self.img, batch_size = None)
        prediction = np.squeeze(prediction)

        print('prediction: {}'.format(int(round(prediction[0])) ))

        return int(round(prediction[0]))


    def img_prep(self, img):
        img = cv2.resize(img,
                              (self.height, self.width),
                              interpolation = cv2.INTER_CUBIC)
        img = self.img_array(img)

        return img

    
    def img_array(self, img):
        img_array = []
        img_array.append(img)
        img_array = np.asarray(img_array, dtype = 'float32')

        return img_array / 255
        
