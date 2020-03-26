from generate import generate
from read import read
from initial_population import init_population
from Population import Population
from Individual import Individual
from crossover import crossover
from mutation import mutate
import matplotlib.pyplot as plt

POPULATION_SIZE = 100
NUMBER_OF_ITEMS = 1100
WEIGHT_MAX = 10030
SIZE_MAX = 10020
OUTPUT_FILE = "generated_data.csv"
ITERATIONS = 50

CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.01
TOURNAMENT_SIZE = 10


def main():
    generate(n=NUMBER_OF_ITEMS, w=WEIGHT_MAX, s=SIZE_MAX, output_file=OUTPUT_FILE)
    all_results = []
    for j in range(4):
        mut = [0.01, 0.1, 0.05, 0.2]
        tour = [5, 10, 40, 90]
        cross = [0.1, 0.3, 0.6, 0.9]
        result = genetic_algorithm(tournament_size=tour[j])
        lab = "tournament_size = " + str(tour[j])
        plt.plot(result, label=lab)
    plt.xlabel("Number of generation")
    plt.ylabel("Best individual")
    tit = "Plot for different tournament sizes"
    plt.title(tit)
    plt.legend()
    plt.show()


def genetic_algorithm(tournament_size=TOURNAMENT_SIZE, crossover_rate=CROSSOVER_RATE, mutation_rate=MUTATION_RATE,
                      population_size=POPULATION_SIZE):
    task = read(input_file=OUTPUT_FILE)
    population = init_population(NUMBER_OF_ITEMS, population_size)
    best_ind = []
    i = 0
    new_pop_val = []
    while i < ITERATIONS:
        # print(i)
        j = 0
        new_pop_arr = []

        while j < population_size:
            parent1 = population.tournament(tournament_size, task)
            parent2 = population.tournament(tournament_size, task)
            child = crossover(parent1, parent2, crossover_rate)
            mutated_child = mutate(child, mutation_rate)
            new_pop_arr.append(mutated_child)
            j += 1
        population = Population(new_pop_arr)
        i += 1
        best_from_pop = population.tournament(population_size, task)
        best_evaluated = best_from_pop.best_individual(task)
        new_pop_val.append(best_evaluated)
    return new_pop_val


if __name__ == "__main__":
    main()
