from Functions.base_function import Base_function

import numpy as np

class Generalized_penalized_function(Base_function):
    def __init__(self,name = 'Generalized_penalized_function',lower_bound = -50,upper_bound = 50,dimension = 30):
        super().__init__(name,lower_bound,upper_bound,dimension)

    def get_fitness(self, x):
        sum1=0
        for i in range(self.dimension):
            y=self.yi(x[i])
            if(i< self.dimension-1):
                sum1=((y-1)**2)*(1+10*(np.sin(np.pi*self.yi(x[i+1]))**2))
            else:
                sum1+= (y-1)**2

        return (np.pi/self.dimension)*(10*np.sin(np.pi*self.yi(x[1]))+sum1)+sum( list( map(lambda x: self.u(x,10,100,4) ,x) ) )

    def yi(self,x):
        return 1 + (x+1)/4

    def u(self,x,a,k,m):
        if(x<a):
            return k*(x-a)**m
        elif(x<-a):
            return k*(-x-a)**m
        else:
            return 0