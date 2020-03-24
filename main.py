from generate import generate
from read import read
from initial_population import init_population
from Population import Population
from Individual import Individual


POPULATION_SIZE = 100
NUMBER_OF_ITEMS = 1100
WEIGHT_MAX = 10030
SIZE_MAX = 10020
OUTPUT_FILE = "generated_data.csv"


def main():
    generate(n=NUMBER_OF_ITEMS, w=WEIGHT_MAX, s=SIZE_MAX, output_file=OUTPUT_FILE)
    task = read(input_file=OUTPUT_FILE)
    # print(task)
    population = init_population(NUMBER_OF_ITEMS, POPULATION_SIZE)
    # print(population.array_of_individuals[0].evaluate())
    tournament = population.tournament(100, task)
    print(int(tournament))



if __name__ == "__main__":
    main()
