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
