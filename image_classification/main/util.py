import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
from io import BytesIO

def image_to_numpy(image_path):
    npimg = Image.open(image_path).convert("RGB")
    npimg = npimg.resize((228, 228), Image.ANTIALIAS)
    npimg = keras.preprocessing.image.img_to_array(npimg)
    npimg = np.array([npimg])
    print(npimg.shape)
    return npimg / 255.

def get_prediction(npimage):
    class_map = {"0":"Cat", "1":"Dog"}
    model_path = '/home/abhinavchat/workspace/tutorials/image_classification/image_classification/assets/cat_dog.h5'
    print(model_path)
    model = keras.models.load_model(model_path)
    k = model.predict(npimage)
    print(k)
    p = np.argmax(keras.utils.to_categorical(k>0.5), axis=-1)
    print(class_map[str(p[0])])
    return class_map[str(p[0])]