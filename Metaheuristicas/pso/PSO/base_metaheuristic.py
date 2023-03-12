from abc import ABC, abstractmethod
from functools import cmp_to_key

class base_metaheuristic(ABC):
    def __init__(self, optimization_problem):
        self.optimization_problem = optimization_problem
        self.global_best = None
    
    @abstractmethod
    def run_metaheuristic():
        pass
    
    #Fixme : donde poner la cantidad de particulas?, aqui o en el swarm?
    def initialize_values(self, all_values):
        if(len(all_values) == 0):
            all_values = list(map(lambda x: self.optimization_problem.random_solution(), range(100) ))
        
        return all_values

    def sort_values(self, all_values):
        return sorted(all_values,key=cmp_to_key(self.compare_values))

    def compare_values(self, value_1, value_2):
        if self.calcule_fitness(value_1) < self.calcule_fitness(value_2):
            return -1

        elif self.calcule_fitness(value_1) > self.calcule_fitness(value_2):
            return 1

        return 0
    
    def adjust_values(self, all_values):
        return list( map( lambda x: self.check_domain(x) , all_values) )

    def check_domain(self, value):
        if(value > self.optimization_problem.upper_bound):
            value = self.optimization_problem.upper_bound
            
        elif(value < self.optimization_problem.lower_bound):
            value = self.optimization_problem.lower_bound

        return value

    def get_min_fitness_value(self, all_values):
        return min(self.global_best, min(all_values, key=lambda x: self.optimization_problem.calcule_fitness(x)),key=lambda x: self.optimization_problem.calcule_fitness(x))