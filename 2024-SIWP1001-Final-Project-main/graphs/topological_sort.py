class TopologicalSort:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.vertices
        stack = []

        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

        return stack[::-1]  # Membalik stack untuk urutan topologis

# Contoh Penggunaan
if __name__ == "__main__":
    topo_sort = TopologicalSort(6)
    topo_sort.add_edge(5, 2)
    topo_sort.add_edge(5, 0)
    topo_sort.add_edge(4, 0)
    topo_sort.add_edge(4, 1)
    topo_sort.add_edge(2, 3)
    topo_sort.add_edge(3, 1)

    print("Topological Sort Order:", topo_sort.topological_sort())
