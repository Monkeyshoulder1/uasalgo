import unittest
from graphs import Graphs

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graphs = Graphs()

    def test_dijkstra(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        self.assertEqual(self.graphs.dijkstra(graph, 'A'), {'A': 0, 'B': 1, 'C': 3, 'D': 4})

if __name__ == "__main__":
    unittest.main()
