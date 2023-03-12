from Functions.base_function import Base_function
import numpy as np

class Generalized_rosenbrock_function(Base_function):
    def __init__(self,name = 'Generalized_rosenbrock_function',lower_bound = -30,upper_bound = 30,dimension = 100):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        x0 = x[1:]
        x1 = x[:-1]
        return np.sum(100*np.subtract(x0,x1**2)**2 + np.subtract(x1,1)**2)