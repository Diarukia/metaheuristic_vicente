from Functions.base_function import Base_function
import numpy as np

class Generalized_rastrigin_function(Base_function):
    def __init__(self,name = 'Generalized_rastrigin_function',lower_bound = -5.12,upper_bound = 5.12,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        n = len(x)
        return 10*n + sum(x**2 - 10 * np.cos(2 * np.pi * x))