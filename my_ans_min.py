#!/usr/bin/env python3

#!/usr/bin/env python3

import sys
import math
from unittest.util import sorted_list_difference
import copy

from common import print_tour, read_input



def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)



   
def opt_2(tour, dist):
    N = len(tour)

    while True:
        count = 0
        for i in range(N-2):
            for j in range(i+2, N):
                l1 = dist[tour[i]][tour[i + 1]]
                l2 = dist[tour[j]][tour[(j + 1) % N]]
                l3 = dist[tour[i]][tour[j]]
                l4 = dist[tour[i + 1]][tour[(j + 1) % N]]
                if l1 + l2 > l3 + l4:
                    new_tour = tour[i+1 : j+1]
                    tour[i+1 : j+1] = new_tour[::-1]
                    count += 1
        if count == 0:
            break
    return tour

def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    dist_data={}
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            if distance(cities[i], cities[j]) not in dist_data:
                dist_data [distance(cities[i], cities[j])] = []
            

    current_city = 0
    unvisited_cities = set(range(1,N))
    tour = [current_city]
    tour_distance=0
    while unvisited_cities:
        next_city = min(unvisited_cities,
                            key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        tour_distance+=distance(cities [current_city],cities[next_city])
        current_city = next_city
    opt_2(tour,dist)

    return tour



if __name__ == '__main__':
    # assert len(sys.argv) > 1
    cities=read_input("./input_0.csv")

    tour= solve(cities)
    print_tour(tour)

