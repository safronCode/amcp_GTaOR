
from particle_swarm_optimizer import *

def function_Schaffer_n4(x):
    return 0.5 + (np.cos(np.sin(abs(x[0]**2 - x[1]**2)))**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2

pso = ParticleSwarmOptimizer(Particle,function_Schaffer_n4)
best_position, best_value, iteration_values,iteration_positions = pso.optimize(save_iterations=True,print_iterations=False)
print("Best Position:", best_position)
print("Best Value:", best_value)
pso.plot_pso_convergence(animated=True)
