from functions.base_function import Base_function
import numpy as np
from math import cos, sin

class Discrete_integral_equation(Base_function):
    def __init__(self,name = 'discrete_integral_equation',lower_bound = -100,upper_bound = 100,dimension = 160):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        h = 1 / (self.dimension + 1)

        pt1 = x + (np.array(np.arange(1,self.dimension+1)) * h) + 1

        pt13 = pt1 * pt1 * pt1

        tii = np.array(np.arange(1,self.dimension+1)) * h
        sum1 = 0

        sum2 = np.sum((1 - tii) * pt13)

        fsum = 0
        for i in range(self.dimension) : 
            ti = tii[i]
            ti1 = 1 - ti
            sum1 = sum1 + ti * pt13[i]
            sum2 = sum2 - ti1 * pt13[i]
            fi = x[i] + 0.5 * h * (ti1 * sum1 + ti * sum2)
            fsum = fsum + fi * fi
        return fsum