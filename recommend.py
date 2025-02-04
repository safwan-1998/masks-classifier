#for image preprocessing
import cv2
from keras.preprocessing import image

#for graph plot
import matplotlib.pyplot as plt

#for image generation
from keras.preprocessing.image import ImageDataGenerator

#for data manupilation
import numpy as np

#for model preparation
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D , Flatten, Dense, Dropout
from keras.models import Sequential

data = cv2.imread('filename')
plt.imshow(data)

image_gen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rescale=1/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

classifier = Sequential()
classifier.add(Conv2D(32,(3,3),input_shape = (100,100,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Conv2D(32,(3,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Conv2D(32,(3,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(units=128,activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=1,activation='sigmoid'))
classifier.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

train_image_gen = image_gen.flow_from_directory('dataset/train',target_size=(100,100),batch_size=16,class_mode='binary')
test_image_gen = image_gen.flow_from_directory('dataset/test',target_size=(100,100),batch_size=16,class_mode='binary')

train_image_gen.class_indices

results = classifier.fit_generator(
    train_image_gen,
    epochs=200,
    validation_data=test_image_gen,
)

data = cv2.imread('filename')
dog_img = image.img_to_array(data)
print(dog_img.shape)
dog_img = np.expand_dims(dog_img,axis=0)
dog_img = dog_img/255
classifier.predict_classes(dog_img)

dog_img = image.load_img(dog_file,target_size=(150,150))
dog_img = image.img_to_array(dog_img)
print(dog_img.shape)
dog_img = np.expand_dims(dog_img,axis=0)
dog_img = dog_img/255
classifier.predict_classes(dog_img)

classifier.save('maskss.h5')
