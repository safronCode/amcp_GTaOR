from SimplexMethod.package.helpers import color_print
from package.helpers import *
from package.methods.pso import pso

iteration, gbest_val, gbest, _ = pso(function_Schaffer_n4)

color_print('Результат работы ParticleSwarmOptimizer:','RED')
print(f'Кол-во итераций: {iteration}\n'
      f'Глобально оптимальное решение: {gbest_val[iteration]}\n'
      f'В точке x* = {gbest}')

plot_fval_convergence(gbest_val)
plot_var_convergence(_[0],0)
plot_var_convergence(_[0],1)
animation_convergence(gbest_store=_[0], x_store= _[1])

