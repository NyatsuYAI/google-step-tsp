#!/usr/bin/env python3

from common import format_tour, read_input

import solver_greedy
import solver_random
import my_ans
import my_ans_min
import my_ans_random

CHALLENGES = 6


def generate_sample_output():
    for i in range(CHALLENGES):
        cities = read_input(f'input_{i}.csv')
        for solver, name in ((solver_greedy, 'random'), (solver_random, 'greedy'),(my_ans_min, 'sa')):
            tour = solver.solve(cities)
            with open(f'sample/{name}_{i}.csv', 'w') as f:
                f.write(format_tour(tour) + '\n')
        


if __name__ == '__main__':
    generate_sample_output()
