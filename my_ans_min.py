#!/usr/bin/env python3

#!/usr/bin/env python3

import sys
import math
from unittest.util import sorted_list_difference
import copy

from common import print_tour, read_input



def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def opt_2(tour,cities):
    N=len(tour)
    while True:
        count=0
        for i1 in range(N - 2):
            i2 = i1 + 1
            for j1 in range(i1 + 2, N):
                if j1 == N - 1:
                    j2 = 0
                else:
                    j2 = j1 + 1
                if i1 != 0 or j2 != 0:
                    l1 = distance(cities[i1],cities[i2])
                    l2 = distance(cities[j1],cities[j2])
                    l3 = distance(cities[i1],cities[j1])
                    l4 = distance(cities[i2],cities[j2])
                    print(i1,i2,j1,j2)
                    print(l1+l2,l3+l4)
                    if l1 + l2 > l3 + l4:
                        # つなぎかえる
                        print(tour,count)
                        new_path = tour[i1:j1+1]
                        tour[i1:j1+1] = new_path[::-1]
                        count+=1
        if count == 0: break
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
    opt_2(tour,cities)

    return tour



if __name__ == '__main__':
    # assert len(sys.argv) > 1
    cities=read_input("./input_0.csv")

    tour= solve(cities)
    print(tour)
    print_tour(tour)

