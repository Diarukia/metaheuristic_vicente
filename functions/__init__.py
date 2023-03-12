from functions.sphere_function import Sphere_function
from functions.schwefel_function_2_22 import Schwefel_function_2_22
from functions.schwefel_function_1_2 import Schwefel_function_1_2
from functions.generalized_rosenbrock_function import Generalized_rosenbrock_function
from functions.generalized_schwefel_function_2_26 import Generalized_schwefel_function_2_26
from functions.generalized_rastrigin_function import Generalized_rastrigin_function
from functions.ackley_function import Ackley_function
from functions.generalized_griewank_function import Generalized_griewank_function
from functions.generalized_penalized_function import Generalized_penalized_function
from functions.shekel_foxholes_function import Shekel_foxholes_function

from functions.Six_hump_camel_back_function import Six_hump_camel_back_function

from functions.branin_function import Branin_function
from functions.goldstein_price_function import Goldstein_price_function
from functions.hartman_family_function_1 import Hartman_family_function_1
from functions.hartman_family_function_2 import Hartman_family_function_2

from functions.extended_rosenbrock_function import Extended_rosenbrock_function
from functions.extended_powell import Extended_powell
from functions.penalty_i_function import Penalty_I_function
from functions.variably_dimensioned_function import Variably_dimensioned_function
from functions.linear_full_rank import Linear_full_rank
from functions.discrete_integral_equation import Discrete_integral_equation
from functions.discrete_boundary_value import Discrete_boundary_value
from functions.brown_almost_linear import Brown_almost_linear
from functions.trigonometric_function import Trigonometric_function
def get_functions():
    return [Sphere_function(), Schwefel_function_2_22(),
            Schwefel_function_1_2(), Generalized_rosenbrock_function(),
            Generalized_schwefel_function_2_26(), Generalized_rastrigin_function(),
            Ackley_function(), Generalized_griewank_function(),
            Generalized_penalized_function(), Shekel_foxholes_function(),
            Six_hump_camel_back_function(), Branin_function(), Goldstein_price_function(),
            Hartman_family_function_1(), Hartman_family_function_2(),
            Extended_rosenbrock_function(), Extended_powell(),
            Penalty_I_function(), Variably_dimensioned_function(),
            Linear_full_rank(), Discrete_integral_equation(),
            Brown_almost_linear(),Discrete_boundary_value(),
            Trigonometric_function()]