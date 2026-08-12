import argparse

parser = argparse.ArgumentParser(description='Meow like a cat')
parser.add_argument('-n', default=1, help='number of meows', type=int)
args = parser.parse_args()

for _ in range(args.n):         # args.n contains the number rightafter typing -n
    print('meow')

# I do not need to import sys
# argparse can fetch out what is needed from the Arguments typed in the terminal
# Especially here the argv's must not be in order !!!
# default=1 is helping to avoid the error if there's no input given by the user
