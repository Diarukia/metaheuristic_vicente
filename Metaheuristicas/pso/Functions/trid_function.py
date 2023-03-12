from Functions.base_function import Base_function

import numpy as np
class Trid_function(Base_function):
    #def __init__(self, name = 'Trid_function', lower_bound = -40000, upper_bound = 40000, dimension = 3):
    def __init__(self, name = 'Trid_function', lower_bound = -40000, upper_bound = 40000, dimension = 3):
        super().__init__(name, lower_bound, upper_bound, dimension)
    
    def get_fitness(self, x):
        return np.sum((np.subtract(x,1))**2) - np.sum(np.multiply(x[1:],x[:-1]))
        #return np.subtract( np.sum((np.subtract(x,1))**2) , np.sum(np.multiply(x[1:],x[:-1])) )


