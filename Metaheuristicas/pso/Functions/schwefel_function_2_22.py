from Functions.base_function import Base_function

import numpy as np

class Schwefel_function_2_22(Base_function):
    def __init__(self,name = 'Schwefel_function_2_22',lower_bound = -10,upper_bound = 10,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self, x):
        x = np.absolute(x)
        return np.sum(x)+np.prod(x)
