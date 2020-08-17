import tensorflow as tf
import numpy as np
from tensorflow import keras

def aiSort(l1, l2):
    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')#Not the right code for this case, this code is for numbers not strings
    a = list(map(int, input().split()))
    #xs = np.array(l1, dtype=string)
    #ys = np.array(l2, dtype=string)
    xs = np.array(['1+2', '9-4', '2+1', '2-1', '3+7', '6-3'], dtype=str)
    ys = np.array(['1', '2', '1', '2', '1', '2'], dtype=str)
    model.fit(xs, ys, epochs=500)
    print(model.predict(['12+10']))
