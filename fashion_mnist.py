# -*- coding: utf-8 -*-
"""Fashion_MNist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19mbzDVC1cUzeejfnandPoNqbVDAXmnrQ
"""

import matplotlib.pyplot as plt
import numpy as np

from keras.datasets import fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train.shape

x_test.shape

cat = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle_boot']

set(y_train)

plt.imshow(x_train[425], cmap = 'gray');

plt.figure(figsize=(16,10))
for i in range(25):
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(x_train[i])
  plt.xlabel(cat[y_train[i]])

x_train[1];

x_train[1].shape

# add a colour channel
x_train = np.expand_dims(x_train, axis = -1)
x_test = np.expand_dims(x_test, axis = -1)

x_train[1].shape

from keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3,3), activation= 'relu', input_shape=(28, 28, 1)),
    MaxPool2D((2,2)),
    Conv2D(64, (3,3), activation= 'relu'),
    MaxPool2D((2,2)),
    Conv2D(64, (3,3), activation= 'relu'),
    Flatten(),
    Dense(64, activation= 'relu'),
    Dense(10, activation= 'softmax')
]) # Enclose the layers within a list when initializing the Sequential model

model.summary()

model.compile(loss = 'categorical_crossentropy', metrics = ['accuracy'],
optimizer = 'adam')
history = model.fit(x_train, y_train, epochs = 10, batch_size = 10,
validation_split= 0.2)

loss, accuracy = model.evaluate(x_test, y_test)