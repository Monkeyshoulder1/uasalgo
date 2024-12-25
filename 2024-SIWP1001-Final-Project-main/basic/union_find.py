class UnionFind:
    """
    Implementasi Union Find (Disjoint Set) Algorithm
    dengan optimasi Path Compression dan Union by Rank
    """

    def __init__(self, n):
        """
        Inisialisasi struktur data Union Find
        
        Args:
            n (int): Jumlah elemen dalam set
        """
        # Parent dari setiap elemen
        self.parent = list(range(n))
        
        # Rank untuk optimasi union
        self.rank = [0] * n
        
        # Jumlah set
        self.count = n

    def find(self, x):
        """
        Temukan root dari set dengan path compression
        
        Args:
            x (int): Elemen yang dicari rootnya
        
        Returns:
            int: Root dari set yang berisi x
        """
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Gabungkan dua set
        
        Args:
            x (int): Elemen pertama
            y (int): Elemen kedua
        
        Returns:
            bool: Apakah union berhasil dilakukan
        """
        # Temukan root dari kedua elemen
        root_x = self.find(x)
        root_y = self.find(y)

        # Cek apakah sudah dalam set yang sama
        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        # Gabungkan set
        self.parent[root_y] = root_x

        # Update rank jika perlu
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        # Kurangi jumlah set
        self.count -= 1
        return True

    def connected(self, x, y):
        """
        Periksa apakah dua elemen terhubung
        
        Args:
            x (int): Elemen pertama
            y (int): Elemen kedua
        
        Returns:
            bool: Apakah x dan y dalam set yang sama
        """
        return self.find(x) == self.find(y)

    def get_count(self):
        """
        Dapatkan jumlah set yang tersisa
        
        Returns:
            int: Jumlah set yang masih terpisah
        """
        return self.count

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh dengan 5 elemen
    uf = UnionFind(5)

    # Gabungkan beberapa elemen
    uf.union(0, 1)  # Gabung 0 dan 1
    uf.union(2, 3)  # Gabung 2 dan 3
    uf.union(1, 4)  # Gabung 1 dan 4

    # Periksa koneksi
    print("0 dan 1 terhubung:", uf.connected(0, 1))  # True
    print("0 dan 2 terhubung:", uf.connected(0, 2))  # False
    print("Jumlah set:", uf.get_count())  # 2

    # Gunakan untuk deteksi siklus dalam graph
    graph_edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    cycle_detector = UnionFind(5)
    
    has_cycle = False
    for u, v in graph_edges:
        if not cycle_detector.union(u, v):
            has_cycle = True
            break

    print("Graph memiliki siklus:", has_cycle)