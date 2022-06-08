#!/usr/bin/env python3

import sys
import math
from unittest.util import sorted_list_difference
import random
import copy

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]
    tour_distance=0

    pre_set_cities=[num for num in range(0,N)]
    tour_index={}

    for i in range(N):
        current_city = i
        preset_cities_copy=copy.copy(pre_set_cities)
        preset_cities_copy.remove(i)
        unvisited_cities = set(preset_cities_copy)
        tour = [current_city]
        tour_distance=0
        while unvisited_cities:
            if random.random()>0.15:
                next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
            else:
                next_city = random.choice(list(unvisited_cities))
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            tour_distance+=distance(cities [current_city],cities[next_city])
            current_city = next_city
        tour_index[tour_distance]=tour
    sorted_tour_index=sorted(tour_index.items(), key=lambda x:x[0])

    return sorted_tour_index[0][1]



if __name__ == '__main__':
    # assert len(sys.argv) > 1
    cities=read_input("./input_3.csv")

    tour= solve(cities)
    print_tour(tour)

