class BellmanFord:
    def shortest_path(self, vertices, edges, start):
        distances = [float('inf')] * vertices
        distances[start] = 0

        for _ in range(vertices - 1):
            for u, v, weight in edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Cek untuk siklus negatif
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                print("Graph contains negative weight cycle")
                return None

        return distances

# Contoh Penggunaan
if __name__ == "__main__":
    vertices = 5
    edges = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
    bellman_ford = BellmanFord()
    print("Jarak Terpendek:", bellman_ford.shortest_path(vertices, edges, 0))
