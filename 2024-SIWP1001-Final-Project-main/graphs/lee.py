from collections import deque

class LeeAlgorithm:
    def is_valid(self, x, y, rows, cols, visited, grid):
        """
        Fungsi untuk memeriksa apakah posisi saat ini valid
        """
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] == 1

    def shortest_path(self, grid, src, dest):
        """
        Implementasi Algoritma Lee untuk menemukan jalur terpendek
        dalam grid menggunakan BFS.
        """
        rows = len(grid)
        cols = len(grid[0])

        # Jika titik sumber atau tujuan tidak valid
        if grid[src[0]][src[1]] != 1 or grid[dest[0]][dest[1]] != 1:
            return -1

        # Empat kemungkinan pergerakan: Atas, Bawah, Kiri, Kanan
        row_moves = [-1, 1, 0, 0]
        col_moves = [0, 0, -1, 1]

        # Inisialisasi visited array
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        visited[src[0]][src[1]] = True

        # Antrian untuk BFS (posisi x, y, jarak saat ini)
        queue = deque([(src[0], src[1], 0)])

        # BFS traversal
        while queue:
            x, y, dist = queue.popleft()

            # Jika kita mencapai tujuan, kembalikan jarak
            if (x, y) == dest:
                return dist

            # Periksa semua gerakan yang memungkinkan
            for i in range(4):
                new_x, new_y = x + row_moves[i], y + col_moves[i]

                if self.is_valid(new_x, new_y, rows, cols, visited, grid):
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, dist + 1))

        # Jika tidak ada jalur ditemukan
        return -1


# Contoh Penggunaan
if __name__ == "__main__":
    grid = [
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 0],
        [0, 1, 1, 1]
    ]
    src = (0, 0)  # Titik awal
    dest = (3, 3)  # Titik tujuan

    lee = LeeAlgorithm()
    result = lee.shortest_path(grid, src, dest)
    if result != -1:
        print(f"Jarak terpendek antara {src} dan {dest} adalah {result}")
    else:
        print("Jalur tidak ditemukan")
