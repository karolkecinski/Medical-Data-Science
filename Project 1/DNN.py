from data_model import DataModel
import os
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Activation

training_data = DataModel(200, 1)
#test_data = DataModel(200, 0)

print(training_data.data.shape)

input_shape = (2288, 200, 3, 9)

model = Sequential()
model.add(Conv2D(64, kernel_size = (3, 3), activation='relu', input_shape=input_shape[1:]))
#model.add(MaxPooling2D(pool_size = (2,2), padding = 'valid', strides = (1,1)))

#model.add(Conv2D(64, kernel_size = (3, 3), activation='relu'))
#model.add(MaxPooling2D(pool_size = (2,2), padding = 'valid', strides = (1,1)))

model.add(Flatten())
model.add(Dense(64))
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy", optimizer = "adam", metrics = ['accuracy'])

model.fit(training_data.data, training_data.labels, epochs = 3, batch_size = 64, validation_split = 0.1)