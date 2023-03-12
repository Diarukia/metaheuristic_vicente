from PSO.base_metaheuristic import base_metaheuristic
import numpy as np
import random

class Particle_swarm_optimization(base_metaheuristic):
    def __init__(self, optimization_problem, number_particles = 40, w = 0.729, c1=  1.494, c2 =  1.494):
        super().__init__(optimization_problem)
        self.number_particles = number_particles
        self.w = w
        self.c1 = c1
        self.c2 = c2
    
    def run_metaheuristic(self, all_values):
        all_values = self.initialize_values(all_values)
        self.global_best = min(all_values)
        best_previous_values = all_values
        velocity = list(map(lambda x,y: self.c1*random.random()*np.subtract(x,y) + self.c2*random.random()*np.subtract(self.global_best,y)
                   ,best_previous_values,all_values))
        
        for i in range(200):
            print(i)
            best_previous_values = self.update_best_personal(all_values,best_previous_values)
            self.global_best = self.get_min_fitness_value(all_values)
            velocity = list(map(lambda x,y,z: self.w*x+self.c1*random.random()*np.subtract(y,z) + self.c2*random.random()*np.subtract(self.global_best,z)
                       ,velocity,best_previous_values,all_values))
            all_values = list(map(lambda x,y : x+y, all_values,velocity))
            all_values = self.adjust_values(all_values)
        print('esto es best ',self.global_best)
        return self.optimization_problem.calcule_fitness(self.global_best)



    def update_best_personal(self, all_values, best_previous_values):
        return list(map(lambda x,y: x if(self.optimization_problem.calcule_fitness(x) <  self.optimization_problem.calcule_fitness(y)) else y, 
               all_values, best_previous_values))