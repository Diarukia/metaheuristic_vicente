from Functions.base_function import Base_function
import numpy as np

class Ackley_function(Base_function):
    def __init__(self,name = 'Ackley_function',lower_bound = -32,upper_bound = 32,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        return -20*np.exp(-0.2*np.sqrt(sum(x**2) / self.dimension)) - np.exp(sum(np.cos(2*np.pi * x)) / self.dimension) + 20 + np.exp(1)