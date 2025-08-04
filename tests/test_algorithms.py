import unittest

from graph import Graph
from algorithms import GraphAlgorithms


class TestAlgorithms(unittest.TestCase):
    def setUp(self) -> None:
        self.algorithms = GraphAlgorithms()

    def test_is_cyclic_undirected_true(self):
        g = Graph([(0,1),(1,2),(3,4),(2,0)])
        is_cyclic = self.algorithms.is_cyclic_undirected(g)
        self.assertTrue(is_cyclic)
    
    def test_is_cyclic_undirected_false(self):
        g = Graph([(1,2),(3,4),(5,6)])
        is_cyclic = self.algorithms.is_cyclic_undirected(g)
        self.assertFalse(is_cyclic)
    
    def test_is_cyclic_typemismatch(self):
        g = []
        with self.assertRaises(TypeError):
            self.algorithms.is_cyclic_undirected(g)
    
    def test_djkstra(self):
        g = Graph([
            ('a', 'b', 4), ('a','c',8),('b','d',8),('b','c',11),('c','e',7),('e','d',2)
        ])
        shorted_paths = self.algorithms.dijkstra(g,source='a')
        self.assertCountEqual(shorted_paths, [('c', 8), ('b', 4), ('d', 12), ('e', 14), ('a', 0)])
    
    def test_shortest_distance_between_two_points(self):
        g = Graph([
            ('a', 'b', 4), ('a','c',8),('b','d',8),('b','c',11),('c','e',7),('e','d',2)
        ])
        shortest_distance = self.algorithms.shortest_distance_between_two_points(g, 'a', 'e')
        self.assertEqual(shortest_distance, 14)
    
    def test_shortest_distance_between_two_points_missing_vertex(self):
        g = Graph([
            ('a', 'b', 4), ('a','c',8),('b','d',8),('b','c',11),('c','e',7),('e','d',2)
        ])
        with self.assertRaises(ValueError):
            self.algorithms.shortest_distance_between_two_points(g,'a','z')
        
    def test_is_cyclic_directed(self):
        test_cases = [
            ([(1, 2), (2, 3), (3, 1)], True),
            ([(1, 2), (2, 3), (3, 4)], False),
            ([(1, 2), (2, 3), (4, 5), (5, 4)], True),
            ([(1, 2), (3, 4)], False),
            ([(1, 1)], True),
            ([(1, 2), (2, 3), (3, 1), (4, 5)], True),
            ([], False),
        ]

        for idx, (edges, expected) in enumerate(test_cases, 1):
            with self.subTest(test_case=idx):
                g = Graph(edges=edges, directed=True)
                result = self.algorithms.is_cyclic_directed(g)
                self.assertEqual(result, expected, f"Failed for edges: {edges}")

            assert result == expected, f"Test case {i} failed: got {result}, expected {expected}"