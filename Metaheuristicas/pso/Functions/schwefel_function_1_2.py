from Functions.base_function import Base_function

import numpy as np

class Schwefel_function_1_2(Base_function):
    def __init__(self,name = 'Schwefel_function_1_2',lower_bound = -100,upper_bound = 100,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        y = np.array(np.arange(0,self.dimension))
        x = np.multiply(x,y)
        return np.sum(np.multiply(x,x))
        #return np.sum([np.sum(x[:i]) ** 2 for i in range(len(x))])
