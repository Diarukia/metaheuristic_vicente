from functions.base_function import Base_function
import numpy as np

class Trigonometric_function(Base_function):
    def __init__(self,name = 'trigonometric_function',lower_bound = -100,upper_bound = 100,dimension = 160):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        cos_sum = np.sum(np.cos(x))
        fi = self.dimension - cos_sum + np.array(np.arange(1,self.dimension+1))  * (1 - np.cos(x)) - np.sin(x)
        return np.sum(fi * fi)