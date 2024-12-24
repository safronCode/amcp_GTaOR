import json
from constants import *
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class Particle:
    def __init__(self, bounds):

        self.position = np.array([np.random.uniform(low, high) for low, high in bounds])

        self.velocity = np.zeros_like(self.position)

        self.best_position = np.copy(self.position)

        self.best_value = float('inf')

    def update_velocity(self, global_best_position, inertia, cognitive, social):

        r1 = np.random.random(len(self.position))
        r2 = np.random.random(len(self.position))


        cognitive_velocity = cognitive * r1 * (self.best_position - self.position)

        social_velocity = social * r2 * (global_best_position - self.position)

        self.velocity = inertia * self.velocity + cognitive_velocity + social_velocity

    def update_position(self, bounds):

        self.position += self.velocity

        for i in range(len(self.position)):
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]


class ParticleSwarmOptimizer:
    def __init__(self, particle_class, objective_function, config_filename=None):

        self.particle_class = particle_class
        if config_filename is None:
            self.config = self.load_or_create_config()
        else:
            self.config = self.load_or_create_config(config_filename)
        self.objective_function = objective_function
        self.bounds = self.config['bounds']
        self.num_particles = self.config['num_particles']
        self.num_iterations = self.config['num_iterations']
        self.inertia = self.config['inertia']
        self.cognitive = self.config['cognitive']
        self.social = self.config['social']

        self.swarm = [self.particle_class(self.bounds) for _ in range(self.num_particles)]
        self.global_best_position = np.copy(self.swarm[0].position)
        self.global_best_value = float('inf')

    def load_or_create_config(self, filename=CONFIG_FILENAME):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                config = json.load(f)
                print("Loaded configuration from", filename)
        else:
            with open(filename, 'w') as f:
                default_config = {DEFAULT_CONFIG_NAMES[i]: DEFAULT_PARTICLE[i] for i in range(len(DEFAULT_PARTICLE))}
                json.dump(default_config, f, indent=4)
                config = default_config
                print(f"Configuration file not found. Created default config at {filename}")
        return config

    def optimize(self, save_iterations=False, print_iterations=False):
        if save_iterations:
            best_values_per_iteration = np.zeros(self.num_iterations)
            best_positions_per_iteration = np.zeros((self.num_iterations, len(self.bounds)))

        for iteration in range(self.num_iterations):
            for particle in self.swarm:
                value = self.objective_function(particle.position)

                if value < particle.best_value:
                    particle.best_value = value
                    particle.best_position = np.copy(particle.position)

                if value < self.global_best_value:
                    self.global_best_value = value
                    self.global_best_position = np.copy(particle.position)

            if save_iterations:
                best_values_per_iteration[iteration] = self.global_best_value
                best_positions_per_iteration[iteration] = np.copy(self.global_best_position)

            for particle in self.swarm:
                particle.update_velocity(self.global_best_position, self.inertia, self.cognitive, self.social)
                particle.update_position(self.bounds)

            if print_iterations:
                print(f"Iteration {iteration + 1}/{self.num_iterations}, Global Best Value: {self.global_best_value}")

        # Возвращаем лучшие значения и позиции для каждой итерации, если save_iterations=True
        if save_iterations:
            self.best_values_per_iteration = best_values_per_iteration
            self.best_positions_per_iteration = best_positions_per_iteration
            return self.global_best_position, self.global_best_value, self.best_values_per_iteration, self.best_positions_per_iteration
        else:
            return self.global_best_position, self.global_best_value, None, None

    def plot_pso_convergence(self, animated=False, gif_name="pso_convergence.gif"):
        """
        Строит график сходимости алгоритма PSO с контурным графиком целевой функции.

        Параметры:
        - objective_function: целевая функция для построения контурного графика.
        - animated: если True, создает анимированный GIF, показывающий процесс сходимости с движением частиц.
        - gif_name: имя GIF-файла для сохранения, если animated=True.
        """
        objective_function = self.objective_function
        iteration_values = self.best_values_per_iteration
        iteration_positions = self.best_positions_per_iteration

        x = np.linspace(self.bounds[0][0], self.bounds[0][1], 100)
        y = np.linspace(self.bounds[1][0], self.bounds[1][1], 100)
        X, Y = np.meshgrid(x, y)
        Z = np.array([[objective_function([x_val, y_val]) for x_val in x] for y_val in y])

        if animated:
            fig, ax = plt.subplots()

            contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
            plt.colorbar(contour, ax=ax)


            particles = ax.scatter([], [], c='blue', label="Particles", s=50)
            global_best = ax.scatter([], [], c='red', label="Global Best", s=100, marker='x')

            ax.set_title("PSO Particle Movement and Convergence")
            ax.set_xlabel("X Position")
            ax.set_ylabel("Y Position")

            def init():
                particles.set_offsets(np.empty((0, 2)))
                global_best.set_offsets(np.empty((0, 2)))
                return particles, global_best

            def update(frame):

                particle_positions = iteration_positions[frame]
                particles.set_offsets(particle_positions)


                global_best_position = iteration_positions[frame]
                global_best.set_offsets(global_best_position)

                return particles, global_best

            ani = animation.FuncAnimation(fig, update, frames=len(iteration_positions), init_func=init, blit=True)


            ani.save(gif_name, writer='imagemagick', fps=5)
            print(f"Animation saved as {gif_name}")

        else:

            fig, ax = plt.subplots()

            contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
            plt.colorbar(contour, ax=ax)

            plt.plot(iteration_values, marker='o', linestyle='-', color='b')
            plt.title("PSO Convergence Plot")
            plt.xlabel("Iterations")
            plt.ylabel("Global Best Value")
            plt.grid(True)
            plt.show()