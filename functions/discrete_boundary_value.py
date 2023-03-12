from functions.base_function import Base_function

import numpy as np
class Discrete_boundary_value(Base_function):
    def __init__(self, name = 'Discrete_boundary_value', lower_bound = -100, upper_bound = 100, dimension = 160):
        super().__init__(name, lower_bound, upper_bound, dimension)
        self.count = 0
    
    def get_fitness(self, x):
      h = 1 / (self.dimension + 1)
      hsq = h * h
      ti = (np.array(np.arange(1,self.dimension+1))) * h
      pt1 = x + ti + 1

      fi = 2 * x + hsq * 0.5 * pt1 * pt1 * pt1
      fi[1:(self.dimension - 1)] = fi[1:(self.dimension - 1)] - x[2:self.dimension]
      fi[2:self.dimension] = fi[2:self.dimension] - x[1:(self.dimension - 1)]
      fsum = sum(fi * fi)
      return fsum
