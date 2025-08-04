from typing import List, Tuple, Any, Dict, Union, Set
from collections import deque

type edgeType = List[Union[List[Tuple[Any, Any]], List[Tuple[Any,Any,int]]]]

class Graph:
    def __init__(self, edges: edgeType, directed: bool = False):
        """
        Represents a Graph with methods to generate the adjacency list and adjacency matrix format.
        Args:
            edges (List[Tuple[Any, Any]]): The list of edges, where each edge is provided as (u,v) where u and v are verticies
            directed (bool, optional): Indicates whether the edges are directed or not. Defaults to False.
        """
        normalized_edges = []
        for edge in edges:
            if not isinstance(edge, tuple) or len(edge) not in (2,3):
                raise ValueError("The edges has to be passed as a list of Tuples of either (u,v) or (u,v,w) where u & v are vertices and w is edge weight")
            u,v = edge[:2]
            w = edge[2] if len(edge) == 3 else 1
            if not isinstance(w, (int,float)):
                raise ValueError("Weight value must be Integer or Float")
            normalized_edges.append((u,v,w))
        self.edges = normalized_edges
        self.directed = directed
        self.vertices = self._extract_vertices(self.edges)

    def _extract_vertices(self,edges: edgeType) -> set:
        """Extract a set of verticies from the edge list. 

        Args:
            edges (List[Tuple[Any, Any]]): The list of edges, where each edge is provided as (u,v) where u and v are verticies

        Returns:
            set: Set of Verticies
        """
        vertices = set()
        for (u, v, w) in edges:
            vertices.add(u)
            vertices.add(v)
        return vertices

    def is_directed(self) -> bool:
        """This function is used to check whether the user provided graph is directed or undirected. 

        Returns:
            bool: Return true if the graph is directed, false otherwise. 
        """
        return self.directed

    def adjacency_list(self) -> Dict[Any, List[Any]]:
        """
        Generate an Adjacency list based on the verticies and edges. 

        Returns:
            Dict[Any, List[Any]]: Dictonary where verticies are keys and the edges are stores as a list
        """

        adj_list = {v: [] for v in self.vertices}
        for u, v, w in self.edges:
            adj_list[u].append((v,w))
            if not self.directed and u != v:
                adj_list[v].append((u,w))
        return adj_list

    def adjacency_list_no_weights(self) -> Dict[Any, Set[Any]]:
        """This function is used to return an adjacency list without weights or the assumed weights is 1

        Returns:
            Dict[Any, Set[Any]]: A dict of vertices as keys and their neighbors as values. 
        """
        adj_list = {v: set() for v in self.vertices}
        for u,v,w in self.edges:
            adj_list[u].add(v)
            if not self.directed and u != v:
                adj_list[v].add(u)
        
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
        for u, v,w in self.edges:
            i, j = idx_mapping[u], idx_mapping[v]
            matrix[i][j] = w
            if not self.directed and i != j:
                matrix[j][i] = w
        
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
                for neighbor, w in adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return order
    
    def dfs(self, start_vertex: Any) -> List[Any]:
        """This method performs the Depth-First Search on the Graph from a given vertex and returns the order. 
        
        Args:
            start (Any): The starting vertex to begin DFS

        Returns:
            List[Any]: The DFS-order of elements starting from the start vertex.
        """ 
        adj_list = self.adjacency_list()
        
        #Check if start_vertex is present in the graph before proceeding 
        if start_vertex not in adj_list:
            raise ValueError(f"Given Start Vertex {start_vertex} is not present in the graph.")
        
        visited = set()
        order = []
        
        def _dfs_recursive(vertex):
            visited.add(vertex)
            order.append(vertex)
            for neighbor,w in adj_list[vertex]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)
        
        _dfs_recursive(start_vertex)
        return order
        
    def __repr__(self):
        return f"Graph has {len(self.vertices)} vertices, {len(self.edges)} edges and is {"directed" if self.directed else "undirected"}"