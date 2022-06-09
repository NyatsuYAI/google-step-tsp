#!/usr/bin/env python3

#!/usr/bin/env python3

import sys
import math
from unittest.util import sorted_list_difference
import copy
import random

from anyio import TypedAttributeLookupError

from common import print_tour, read_input

from common import format_tour


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)



   
def opt_2(tour, dist,tour_distance):
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
                    tour_distance-=(l1+l2)
                    tour_distance+=(l3+l4)
                    count += 1
        if count == 0:
            break
    return tour, tour_distance

def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    dist_data={}
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            if distance(cities[i], cities[j]) not in dist_data:
                dist_data [distance(cities[i], cities[j])] = []
            

    

    random_check_city=set(range(0,N))
    for k in range(int(N/5)):
        if len(random_check_city)<50:
            random_check_city.add(random.randint(0,N-1))
        else:
            break
    print(random_check_city)
    pre_set_cities=[num for num in range(0,N)]
    tour_index={}
    for current_city in random_check_city:
        preset_cities_copy=copy.copy(pre_set_cities)
        preset_cities_copy.remove(current_city)
        unvisited_cities = set(preset_cities_copy)
        tour = [current_city]
        tour_distance=0
        while unvisited_cities:
            next_city = min(unvisited_cities,
                                key=lambda city: dist[current_city][city])
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            tour_distance+=dist[current_city][next_city]
            current_city = next_city

        tour,tour_distance = opt_2(tour,dist,tour_distance)
        tour_index[tour_distance]=tour
        print(tour_distance)

    sorted_tour_index=sorted(tour_index.items(), key=lambda x:x[0])

    return sorted_tour_index[0][1]



if __name__ == '__main__':
    # assert len(sys.argv) > 1
    cities=read_input("./input_6.csv")
    tour= solve(cities)

    print_tour(tour)
