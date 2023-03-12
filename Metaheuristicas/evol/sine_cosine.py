from functions.sphere_function import Sphere_function
import math
import random 
import copy
def sine_cosine_algorithm():
    max_iterations = 10000
    N = crear_poblacion(10)
    best = best_position(N)
    A = 2

    for i in range(max_iterations):
        r1 = A - (i*(A/max_iterations))
        v = copy.deepcopy(N)
        for j in range(len(v)):
            r2 = random.uniform(0, 2*math.pi)
            r3 = random.uniform(0,2)
            if(random.random() < 0.5):
                v[j] = v[j] + r1*math.sin(r2) + abs(r3*best - N[j])
            else:
                v[j] = v[j] + r1*math.cos(r2) + abs(r3*best - N[j])

        for k in range(len(N)):
            if(Sphere_function().calcule_fitness(N[k]) > Sphere_function().calcule_fitness(v[k])):
                    N[k] = v[k]
            
        best = best_position(N)

    return Sphere_function().calcule_fitness(best)


def best_position(valores):
    best = valores[0]
    for i in range(len(valores)):
        if( Sphere_function().calcule_fitness(best) > Sphere_function().calcule_fitness(valores[i])):
            best = valores[i]
    return best

def crear_poblacion(cuantos):
    poblacion = list()
    for i in range(cuantos):
        random = Sphere_function().random_solution()
        poblacion.append(random)
    return poblacion

def imprimir_fitness(valores):
    for i in range(len(valores))   :
        print(Sphere_function().calcule_fitness(valores[i]))

def main():
    print(sine_cosine_algorithm())

main()