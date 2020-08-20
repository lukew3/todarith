import tensorflow as tf
import numpy as np
from tensorflow import keras


def createModel(problems, answers):
    train_answers = [] #convert str to int
    train_problems = []
    for item in l1:
        train_problems.append(mathEncoder(item))
    model = keras.Sequential([
        keras.layers.Dense(5, activation='relu'),
        keras.layers.Dense(4)
    ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    model.fit(train_problems, train_skills, epochs=1000)
    model.save('models/gen/v1')

def mathEncoder(mathString):
    mathDict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '(': 10,
        ')': 11,
        '+': 12,
        '-': 13,
        '*': 14,
        '/': 15,
        '=': 16,
        '^': 17,
        '[': 18,
        ']': 19,
    }
    encoded_math = []
    for char in mathString:
        encoded_math.append(mathDict.get(char))
    while len(encoded_math) < 5:
        encoded_math.append(20)
    return encoded_math
