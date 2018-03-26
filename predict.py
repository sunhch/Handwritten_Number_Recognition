import tensorflow as tf
import numpy as np
from PIL import Image

from model import Network

'''
python 3.6
tensorflow 1.4
pillow(PIL) 4.3.0

'''

CKPT_DIR = 'ckpt'


class Predict:
    def __init__(self):
        self.net = Network()
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())


        self.restore()

    def restore(self):
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(CKPT_DIR)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(self.sess, ckpt.model_checkpoint_path)
        else:
            raise FileNotFoundError("No model")

    def predict(self, image_path):
        
        basewidth = 28
        img = Image.open(image_path).convert('L')
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        flatten_img = np.reshape(img, 784)
        x = np.array([1 - flatten_img])
        y = self.sess.run(self.net.y, feed_dict={self.net.x: x})

        
        print(image_path)
        out = np.argmax(y[0])
        print('        -> Predict digit', out)
        return out


if __name__ == "__main__":
    app = Predict()
    app.predict('images/0.png')
    app.predict('images/1.png')
    app.predict('images/5.png')
    app.predict('images/4.png')
    app.predict('images/9.png')

