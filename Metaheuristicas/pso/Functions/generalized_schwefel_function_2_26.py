from Functions.base_function import Base_function

import numpy as np

class Generalized_schwefel_function_2_26(Base_function):
    def __init__(self,name = 'Generalized_schwefel_function_2_26',lower_bound = -500,upper_bound = 500,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        return -np.sum(x * np.sin(np.sqrt(np.absolute(x))))

