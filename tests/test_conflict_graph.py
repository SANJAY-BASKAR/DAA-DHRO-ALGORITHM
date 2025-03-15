import unittest
import networkx as nx
from dhro_algorithm import construct_conflict_graph

class TestConflictGraph(unittest.TestCase):
    def test_graph_nodes(self):
        exams = {
            'Math': ['Alice', 'Bob'],
            'Physics': ['Bob', 'Charlie']
        }
        graph = construct_conflict_graph(exams)
        self.assertEqual(len(graph.nodes), 2)
        self.assertEqual(len(graph.edges), 1)

if __name__ == '__main__':
    unittest.main()
