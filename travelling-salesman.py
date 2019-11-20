import numpy as np
import matplotlib.pyplot as plt
from utils.genetic_algorithm import *
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--n-cities", help="Number of Cities", default="20")
parser.add_argument("-x", "--cross-rate", help="Cross Rate", default="0.1")
parser.add_argument("-m", "--mut-rate", help="Mutation Rate", default="0.02")
parser.add_argument("-p", "--pop-size", help="Size of Population", default="500")
parser.add_argument("-g", "--gens", help="Number of Generation", default="500")
parser.print_help()

if __name__ == "__main__":
    args = parser.parse_args()
    N_CITIES = int(args.n_cities)
    CROSS_RATE = float(args.cross_rate)
    MUTATE_RATE = float(args.mut_rate)
    POP_SIZE = int(args.pop_size)
    N_GENERATIONS = int(args.gens)

#     print(N_CITIES, CROSS_RATE, MUTATE_RATE, POP_SIZE, N_GENERATIONS)
    ga = GA(DNA_size=N_CITIES, cross_rate=CROSS_RATE, mutation_rate=MUTATE_RATE, pop_size=POP_SIZE)

    env = TravelSalesPerson(N_CITIES)

    for generation in range(N_GENERATIONS):
        lx, ly = ga.translateDNA(ga.pop, env.city_position)
        fitness, total_distance = ga.get_fitness(lx, ly)
        ga.evolve(fitness)
        best_idx = np.argmax(fitness)
        print('Gen:', generation, '| best fit: %.2f' % fitness[best_idx],)

        env.plotting(lx[best_idx], ly[best_idx], total_distance[best_idx])

    plt.ioff()
    plt.show()