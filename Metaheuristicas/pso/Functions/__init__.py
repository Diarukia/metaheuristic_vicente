from Functions.sphere_function import Sphere_function
from Functions.schwefel_function_2_22 import Schwefel_function_2_22
from Functions.schwefel_function_1_2 import Schwefel_function_1_2
from Functions.generalized_rosenbrock_function import Generalized_rosenbrock_function
from Functions.generalized_schwefel_function_2_26 import Generalized_schwefel_function_2_26

def get_functions():
    return [Sphere_function(), Schwefel_function_2_22(),
            Schwefel_function_1_2(), Generalized_rosenbrock_function(),
            Generalized_schwefel_function_2_26()]