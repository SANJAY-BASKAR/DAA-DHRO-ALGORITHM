import unittest
from dhro_algorithm import greedy_coloring

class TestScheduling(unittest.TestCase):
    def test_coloring(self):
        graph = {
            'Math': {'Physics'},
            'Physics': {'Math', 'Chemistry'},
            'Chemistry': {'Physics'}
        }
        coloring = greedy_coloring(graph)
        self.assertNotEqual(coloring['Math'], coloring['Physics'])
        self.assertNotEqual(coloring['Physics'], coloring['Chemistry'])

if __name__ == '__main__':
    unittest.main()
