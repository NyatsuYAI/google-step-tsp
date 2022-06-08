
import sys
import math
from unittest.util import sorted_list_difference
import copy

from common import print_tour, read_input



def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)



def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    dist_data={}
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            if distance(cities[i], cities[j]) not in dist_data:
                dist_data [distance(cities[i], cities[j])] = []
            

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
            next_city = min(unvisited_cities,
                            key=lambda city: dist[current_city][city])
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            tour_distance+=distance(cities [current_city],cities[next_city])
            current_city = next_city
        tour_index[tour_distance]=tour
    sorted_tour_index=sorted(tour_index.items(), key=lambda x:x[0])
    return sorted_tour_index[0][1]



if __name__ == '__main__':
    # assert len(sys.argv) > 1
    cities=read_input("./input_0.csv")

    tour= solve(cities)
    print_tour(tour)
