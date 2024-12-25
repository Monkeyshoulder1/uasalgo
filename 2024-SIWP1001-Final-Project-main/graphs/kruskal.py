class Kruskal:
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def minimum_spanning_tree(self, vertices, edges):
        result = []
        edges.sort(key=lambda x: x[2])
        parent = [i for i in range(vertices)]
        rank = [0] * vertices

        for u, v, weight in edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                result.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)
        
        return result

# Contoh Penggunaan
if __name__ == "__main__":
    vertices = 4
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    kruskal = Kruskal()
    print("Minimum Spanning Tree:", kruskal.minimum_spanning_tree(vertices, edges))
