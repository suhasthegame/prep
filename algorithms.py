from graph import Graph
from typing import List, Tuple, Any
class GraphAlgorithms:
    def __init__(self) -> None:
        pass

    def is_cyclic_undirected(self,g: Graph) -> bool:
        """This function will use DFS algorithm to detect whether a cycle is present in an undirected graph

        Args:
            g (Gaph): An object of graph class that is capable of providing the Adjaceny_list format of graph

        Returns:r
            bool: Returns true if a cycle is present, else false
        """
        #Make sure the graph is an object of the expected class
        if not isinstance(g, Graph):
            raise TypeError(f"Provide a graph that is an instance of the Graph Class")

        adj_list = g.adjacency_list()

        #Checking if graph is empty. If empty, return False
        if not len(adj_list):
            return False
        
        vertices = adj_list.keys()

        def _check_cycle(vertex,visited,parent) -> bool:
            """Helper function that performs DFS recursively in order to find whether a cycle exists in a graph or not.

            Args:
                vertex (Any): The vertex in the graph
                visited (set): A set to track the visited nodes when performing DFS
                parent (Any): The vertex that is the immediate parent of the neighboring node. 

            Returns:
                bool: Return true if a cycle exists, false otherwise. 
            """
            visited.add(vertex)

            for neighbor,w in adj_list[vertex]:
                if neighbor not in visited:
                    if _check_cycle(neighbor, visited, vertex):
                        return True
                elif neighbor != parent:
                    return True

            return False
            
        
        visited = set()
        for vertex in vertices:
            if vertex not in visited:
                if _check_cycle(vertex, visited, -1):
                    return True
            
        return False

    # def dijkstra(self,graph:Graph, source: Any) -> List[Tuple[Any, int]]:
    #     if not isinstance(graph, Graph):
    #         raise TypeError(f"")
            