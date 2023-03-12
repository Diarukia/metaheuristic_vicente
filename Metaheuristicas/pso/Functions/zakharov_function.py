from Functions.base_function import Base_function

import numpy as np
class Zakharov_function(Base_function):
    def __init__(self, name = 'Zakharov_function', lower_bound = -5, upper_bound = 10, dimension = 200):
        super().__init__(name, lower_bound, upper_bound, dimension)
    
    def get_fitness(self, x):
        j = np.array(np.arange(0,self.dimension))
        return np.sum(np.multiply(x,x)) + np.power(np.sum(0.5*np.multiply(j,x)),2) + np.power(np.sum(0.5*np.multiply(j,x)),4)


