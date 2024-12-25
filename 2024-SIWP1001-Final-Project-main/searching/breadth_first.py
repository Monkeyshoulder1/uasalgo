from collections import deque

class BFS:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque([start])
        visited[start] = True

        print("BFS Traversal:")
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Contoh Penggunaan
if __name__ == "__main__":
    bfs = BFS(4)
    bfs.add_edge(0, 1)
    bfs.add_edge(0, 2)
    bfs.add_edge(1, 2)
    bfs.add_edge(2, 0)
    bfs.add_edge(2, 3)
    bfs.add_edge(3, 3)

    bfs.bfs(2)
