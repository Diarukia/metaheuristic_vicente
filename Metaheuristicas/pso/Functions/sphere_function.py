from Functions.base_function import Base_function

import numpy as np
import math
class Sphere_function(Base_function):
    def __init__(self, name = 'Sphere_function', lower_bound = -100, upper_bound = 100, dimension = 100):
        super().__init__(name, lower_bound, upper_bound, dimension)
    
    def get_fitness(self, x):
        return np.sum(np.multiply(x,x))


