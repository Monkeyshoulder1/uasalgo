class DFS:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recursive(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start):
        visited = [False] * self.vertices
        print("DFS Traversal:")
        self.dfs_recursive(start, visited)

# Contoh Penggunaan
if __name__ == "__main__":
    dfs = DFS(4)
    dfs.add_edge(0, 1)
    dfs.add_edge(0, 2)
    dfs.add_edge(1, 2)
    dfs.add_edge(2, 0)
    dfs.add_edge(2, 3)
    dfs.add_edge(3, 3)

    dfs.dfs(2)
