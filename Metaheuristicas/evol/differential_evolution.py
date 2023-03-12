from functions.sphere_function import Sphere_function

import random 

def evolucion_diferencial():
    N = crear_poblacion(10)
    CR = 0.5
    F = 0.7
    for i in range(100):
        #usa current to best
        v = mutation(N, F)
        for j in range(len(v)):
            if(random.uniform(0, 1) <= CR or j == random.randrange(len(v)) ):
                if(Sphere_function().calcule_fitness(v[j]) <= Sphere_function().calcule_fitness(N[j])):
                    N[j] = v[j]
        
    print(Sphere_function().calcule_fitness(N[0]))   
    return N

def best_position(valores):
    best = valores[0]
    for i in range(len(valores)  ):
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


def mutation(N, F):
    v = list()
    for i in range(len(N)):
        r1 = random.randrange(len(N))
        r2 = random.randrange(len(N))
        v.append( best_position(N)+F*(N[r1]-N[r2]) )
    return v

def main():
    evolucion_diferencial()

main()