# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 14:17:33 2025

@author: gojef
"""
import keras 
import tens as tf
class MyDenseLayer (tf.keras.layers, Layer):
    def __init__(self, input_dim, output_dim):
        super(MyDenseLayer, self).__init__()
        
        #initialize weights and bias
        self.W = self.add_weights([input_dim, output_dim])
        self.b = self.add_weights([1, output_dim])