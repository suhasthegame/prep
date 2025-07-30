from typing import List, Tuple, Any, Dict
from collections import deque

class Graph:
    def __init__(self, edges: List[Tuple[Any, Any]], directed: bool = False):
        """
        Represents a Graph with methods to generate the adjacency list and adjacency matrix format.
        Args:
            edges (List[Tuple[Any, Any]]): The list of edges, where each edge is provided as (u,v) where u and v are verticies
            directed (bool, optional): Indicates whether the edges are directed or not. Defaults to False.
        """
        self.edges = edges
        self.directed = directed
        self.vertices = self._extract_vertices(edges)

    def _extract_vertices(self,edges: List[Tuple[Any, Any]]) -> set:
        """Extract a set of verticies from the edge list. 

        Args:
            edges (List[Tuple[Any, Any]]): The list of edges, where each edge is provided as (u,v) where u and v are verticies

        Returns:
            set: Set of Verticies
        """
        vertices = set()
        for (u, v) in edges:
            vertices.add(u)
            vertices.add(v)
        return vertices

    def adjacency_list(self) -> Dict[Any, List[Any]]:
        """
        Generate an Adjacency list based on the verticies and edges. 

        Returns:
            Dict[Any, List[Any]]: Dictonary where verticies are keys and the edges are stores as a list
        """

        adj_list = {v: [] for v in self.vertices}
        for u, v in self.edges:
            adj_list[u].append(v)
            if not self.directed and u != v:
                adj_list[v].append(u)
        return adj_list

    def adjacency_matrix(self) -> List[List[int]]:
        """
        Generate an Adjacency Matrix based on the verticies and edges

        Returns:
            List[List[int]]: A 2D Matrix with all the edge information population such that matrix[i][j] == 1 indicates whether there exists an edge between i and j.
        """

        vertex_list = sorted(self.vertices)
        idx_mapping = {vertex: i for i, vertex in enumerate(vertex_list)}
        size = len(vertex_list)
        matrix = [[0]*size for _ in range(size) ]
        for u, v in self.edges:
            i, j = idx_mapping[u], idx_mapping[v]
            matrix[i][j] = 1
            if not self.directed and i != j:
                matrix[j][i] = 1
        
        return matrix
    
    def bfs(self,start: Any) -> List[Any]:
        """This method is used to perform Breadth-first search from the given start vertex.

        Args:
            start (Any): The vertex to start the BFS from. 

        Returns:
            List[Any]: List of vertices in the BFS order.
        """

        visited = set()
        queue = deque([start])
        order = []

        adj_list = self.adjacency_list()
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor in adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return order

    def __repr__(self):
        return f"Graph has {len(self.vertices)} vertices, {len(self.edges)} edges and is {"directed" if self.directed else "undirected"}"