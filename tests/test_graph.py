import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def test_adjacency_list(self):
        g = Graph([(1,2),(2,3), (3,1)])
        adj_list = g.adjacency_list()
        #Check whether all the vertices are being added into the vertices list
        self.assertEqual(set(adj_list.keys()), {1,2,3})
        #Since undirected graph, check if the linking between 2 and 1 exists since we only define edge from 1->2
        self.assertIn(2, adj_list[1])
    
    def test_adjacency_matrix(self):
        g = Graph([(1,2), (2,3), (3,1)], directed=True)
        matrix = g.adjacency_matrix()
        self.assertEqual(matrix[0][1],1) #edge 1-> 2
    
    def test_bfs(self):
        g = Graph([(1,2),(3,4),(4,1)])
        order = g.bfs(1)
        self.assertEqual(order, [1,2,4,3])

    def test_dfs(self):
        g = Graph([(1,2), (2,3), (1,4), (3,6)])
        adj_list = g.adjacency_list()
        order = g.dfs(1)
        self.assertEqual(order, [1,2,3,6,4])
if __name__ == "__main__":
    unittest.main()