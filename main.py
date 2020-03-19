from generate import generate
from read import read


def main():
    generate(n=1400, w=10030, s=10020, output_file="generated_data.csv")
    read(input_file="generated_data.csv")


if __name__ == "__main__":
    main()



