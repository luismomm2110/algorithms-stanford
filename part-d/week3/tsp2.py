from math import sqrt

def open_file(path):
    f = open(path, "r")

    num_cities = int(f.readline())

    i = 0
    cities = []
    for city in f.readlines():
        i  = int(city.split()[0]) -1
        distances = list(map(float, city.split()[1:]))
        distances.append(i)
        cities.append(distances)

    return num_cities, cities


def squared_euclidian_distance(origin, destiny):
    return sqrt((destiny[0]- origin[0])**2 + (destiny[1]- origin[1])**2)

def find_nearest_neighbor(origin, next_cities):
    sorted_list = sorted(next_cities, key=lambda x: squared_euclidian_distance(origin, x))
    next_city = next(x for x in sorted_list if x[2] != origin[2])
    return next_city[2]


def tsp(num_cities, cities):
    current_city_index = 0
    path = []
    origin = cities[current_city_index]
    distance = 0

    for _ in range(num_cities):
        if _ == num_cities - 1:
            path.append(current_city_index+1)
            break;
        next_city_index = find_nearest_neighbor(cities[current_city_index], cities)
        distance += squared_euclidian_distance(cities[current_city_index],  cities[next_city_index])
        path.append(current_city_index + 1)
        cities[current_city_index] = [float("inf"), float("inf"), current_city_index] 
        current_city_index = next_city_index


    distance += squared_euclidian_distance(cities[current_city_index], origin)
    path.append(origin[2]+1)


    return int(distance), path



def main():
    num_cities, cities = open_file("p1.txt")
    distance, path = tsp(num_cities, cities)
    print(distance)


if __name__ == "__main__":
    main()
