from functions.base_function import Base_function
import numpy as np

class Brown_almost_linear(Base_function):
    def __init__(self,name = 'Brown_almost_linear',lower_bound = -100,upper_bound = 100,dimension = 160):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
      res = None
      n = len(x)	
      s = sum(x)
      res = x + s - (n+1)
      res[-1] = np.prod(x) - 1
      return np.sum(abs(res))