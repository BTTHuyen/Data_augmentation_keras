import os
#import numpy as np
#import tensorflow as tf
#import cv2
#from PIL import Image
#from matplotlib import pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, array_to_img,  img_to_array, load_img
from numpy import expand_dims
generator = tf.keras.preprocessing.image.ImageDataGenerator(
    zoom_range=0.5, width_shift_range=0.2, brightness_range = (0.5, 1.5), channel_shift_range = 50
)

imgs = os.listdir("Coin_Banknote/images")

for file_name in imgs:
    img=load_img("Coin_Banknote/images/"+file_name)
    x = img_to_array(img)
    #x = x.reshape((1,) + x.shape)
    x = expand_dims(x, 0)

    i = 0
    for batch in generator.flow (x, batch_size=1, save_to_dir =r'new_images4', save_prefix =file_name[:-4]+"br", save_format='jpg'):
        i+=1
        if i>0:
            break
            
