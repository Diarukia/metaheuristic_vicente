from Functions.base_function import Base_function

import numpy as np

class Shekel_foxholes_function(Base_function):
    def __init__(self,name = 'Shekel_foxholes_function',lower_bound = -65.536,upper_bound = 65.536,dimension = 2):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self,x):
        a=[[-32,-32],[-16,-32],[0,-32],[16,-32],[32,-32],[-32,-16],[-16,-16],[0,-16],[16,-16],[32,-16],[-32,0],[-16,0],[0,0],[16,0],[32,0],[-32,16],[-16,16],[0,16],[16,16],[32,16],[-32,32],[-16,32],[0,32],[16,32],[32,32]]
        sum=0
        for i in range(25):
            sumint=0
            for j in range(2):
                sumint+=(x[j]-a[i][j])**6
            sumint+= i
            sum+=(1/sumint)
        sum+=(1/500)
        sum=(1/sum)
        return sum+1
