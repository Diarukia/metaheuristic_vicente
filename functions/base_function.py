import numpy as np
import random
from abc import ABC, abstractmethod

class Base_function(ABC):
    def __init__(self, name, lower_bound, upper_bound, dimension):
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dimension = dimension

    @abstractmethod
    def get_fitness(self, x):
        pass

    def random_solution(self):
        return self.lower_bound+random.random()*(self.upper_bound-self.lower_bound)

    def calcule_fitness(self, x):
        return self.get_fitness( np.asarray_chkfinite( np.full((self.dimension), x, dtype=np.float64) ) )
    
    def get_info(self):
        print("Function name : ", self.name)
        print("Lower bound : ",self.lower_bound)
        print("Upper bound : ", self.upper_bound)
        print("Dimension : ", self.dimension)
