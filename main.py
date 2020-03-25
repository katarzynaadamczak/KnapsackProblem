from generate import generate
from read import read
from initial_population import init_population
from Population import Population
from Individual import Individual
from crossover import crossover
from mutation import mutate

POPULATION_SIZE = 100
NUMBER_OF_ITEMS = 1100
WEIGHT_MAX = 10030
SIZE_MAX = 10020
OUTPUT_FILE = "generated_data.csv"
ITERATIONS = 10

CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.01


def main():
    generate(n=NUMBER_OF_ITEMS, w=WEIGHT_MAX, s=SIZE_MAX, output_file=OUTPUT_FILE)
    a = genetic_algorithm()
    print(a)


def genetic_algorithm():
    task = read(input_file=OUTPUT_FILE)
    population = init_population(NUMBER_OF_ITEMS, POPULATION_SIZE)
    i = 0
    while i < ITERATIONS:
        j = 0
        new_pop_arr = []
        while j < POPULATION_SIZE:
            parent1 = population.tournament(10, task)
            parent2 = population.tournament(10, task)
            child = crossover(parent1, parent2, CROSSOVER_RATE)
            mutated_child = mutate(child, MUTATION_RATE)
            new_pop_arr.append(mutated_child)
            j += 1
        population = Population(new_pop_arr)
        i += 1
    best = population.tournament(POPULATION_SIZE, task)
    return best.best_individual(task)


if __name__ == "__main__":
    main()
