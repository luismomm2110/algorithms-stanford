import tsp2
import math
import unittest


class Test_tsp(unittest.TestCase):
    def test_find_nearest_neighbor_when_not_equal(self):
        origin = [0, 0, 0]
        destines = [[1, 1, 1], [10, 10, 2]]
        self.assertEqual(tsp2.find_nearest_neighbor(origin, destines), 1)

    def test_find_nearest_neightbor_when_distant_come_firt(self):
        origin = [0, 0, 0]
        destines = [[10, 10, 1], [1, 1, 2]]
        self.assertEqual(tsp2.find_nearest_neighbor(origin, destines), 2)


    def test_find_nearest_neighbor_when_equal(self):
        origin = [0, 0, 0]
        destines = [[1, 1, 1], [1, 1, 2]]
        self.assertEqual(tsp2.find_nearest_neighbor(origin, destines), 1)

    def test_squared_euclidian_distance(self):
        origin = [0, 0]
        destiny = [4, 4]

        self.assertEqual(tsp2.squared_euclidian_distance(origin, destiny), math.sqrt(32))


    def test_tsp_distance(self):    
        num_cities, cities = tsp2.open_file("teste.txt")
        self.assertEqual(tsp2.tsp(num_cities, cities)[0], 15)

    def test_tsp_path(self):
        num_cities, cities = tsp2.open_file("teste.txt")
        self.assertEqual(tsp2.tsp(num_cities, cities)[1], [1,3,2,5,6,4,1])