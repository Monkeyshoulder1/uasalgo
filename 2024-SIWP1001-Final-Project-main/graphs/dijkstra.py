import heapq

class Dijkstra:
    def shortest_path(self, graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)
            
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

# Contoh Penggunaan
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    dijkstra = Dijkstra()
    print("Jarak Terpendek:", dijkstra.shortest_path(graph, 'A'))
