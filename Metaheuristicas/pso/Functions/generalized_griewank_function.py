from Functions.base_function import Base_function

import numpy as np

class Generalized_griewank_function(Base_function):
    def __init__(self,name = 'Generalized_griewank_function',lower_bound = -600,upper_bound = 600,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        return sum(x**2)/4000 -  np.prod(np.cos(x / np.sqrt(np.arange(1., self.dimension+1 )))) + 1
