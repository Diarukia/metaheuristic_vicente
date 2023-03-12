from PSO.particle_swarm_optimization import Particle_swarm_optimization
from Functions.linear_full_rank import Linear_full_rank
from Functions.sphere_function import Sphere_function
from Functions.shekel_foxholes_function import Shekel_foxholes_function
from Functions.extended_rosenbrock_function import Extended_rosenbrock_function
from Functions.variably_dimensioned_function import Variably_dimensioned_function
from Functions.penalty_i_function import Penalty_I_function

from Functions.extended_powell_singular_function import Extended_powell_singular_function

import time

if __name__ == '__main__':
    start_time = time.time()
    holi = Particle_swarm_optimization( Shekel_foxholes_function() )
    print(holi.run_metaheuristic( list() ))
    print("--- %s seconds ---" % (time.time() - start_time))


