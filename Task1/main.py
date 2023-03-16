import argparse
from ArmstrongNumsGenerator import ArmstrongNumsGenerator
from RecursiveCalculator import RecursiveCalculator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Armstrong numbers')
    parser.add_argument('start', type=int, default=9, help='starting number')
    parser.add_argument('end', type=int, default=9999, help='ending number')
    args = parser.parse_args()

    generator = ArmstrongNumsGenerator(args.start, args.end)
    armstrong_nums = list(generator.generate())

    for num in armstrong_nums:
        print(num)

    print(RecursiveCalculator.recursive_sum(armstrong_nums))
