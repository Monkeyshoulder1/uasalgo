class HuffmanCoding:
    """
    Implementasi lengkap Algoritma Huffman Coding untuk kompresi data
    """
    
    class Node:
        """
        Kelas internal untuk node pohon Huffman
        """
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None
        
        # Metode untuk membandingkan node
        def __lt__(self, other):
            return self.freq < other.freq

    def calculate_frequency(self, data):
        """
        Hitung frekuensi kemunculan setiap karakter

        Args:
            data (str): String input untuk dianalisis

        Returns:
            dict: Frekuensi setiap karakter
        """
        frequency = {}
        for char in data:
            frequency[char] = frequency.get(char, 0) + 1
        return frequency

    def build_huffman_tree(self, frequency):
        """
        Bangun pohon Huffman dari frekuensi karakter

        Args:
            frequency (dict): Frekuensi kemunculan karakter

        Returns:
            Node: Root dari pohon Huffman
        """
        from heapq import heappush, heappop, heapify

        # Buat heap dari node
        heap = [self.Node(char, count) for char, count in frequency.items()]
        heapify(heap)

        # Bangun pohon
        while len(heap) > 1:
            # Ambil dua node dengan frekuensi terkecil
            left = heappop(heap)
            right = heappop(heap)

            # Buat node internal baru
            merged = self.Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            # Masukkan kembali ke heap
            heappush(heap, merged)

        return heap[0]

    def generate_huffman_codes(self, root):
        """
        Generate kode Huffman untuk setiap karakter

        Args:
            root (Node): Root pohon Huffman

        Returns:
            dict: Kode Huffman untuk setiap karakter
        """
        def traverse(node, current_code):
            if node is None:
                return {}

            # Jika leaf node
            if not node.left and not node.right:
                return {node.char: current_code}

            # Rekursi ke kiri dan kanan
            codes = {}
            codes.update(traverse(node.left, current_code + "0"))
            codes.update(traverse(node.right, current_code + "1"))
            
            return codes

        return traverse(root, "")

    def encode(self, data):
        """
        Enkode data menggunakan kode Huffman

        Args:
            data (str): Data untuk dikodekan

        Returns:
            str: Data terkodekan dalam biner
        """
        # Hitung frekuensi
        freq = self.calculate_frequency(data)
        
        # Bangun pohon
        huffman_tree = self.build_huffman_tree(freq)
        
        # Generate kode
        huffman_codes = self.generate_huffman_codes(huffman_tree)
        
        # Encode data
        encoded_data = ''.join([huffman_codes[char] for char in data])
        
        return encoded_data, huffman_codes

    def decode(self, encoded_data, huffman_codes):
        """
        Dekode data yang telah dikodekan

        Args:
            encoded_data (str): Data biner yang dikodekan
            huffman_codes (dict): Kode Huffman untuk dekoding

        Returns:
            str: Data asli sebelum pengkodean
        """
        # Buat reverse mapping
        reverse_codes = {code: char for char, code in huffman_codes.items()}
        
        current_code = ""
        decoded_data = ""
        
        for bit in encoded_data:
            current_code += bit
            if current_code in reverse_codes:
                decoded_data += reverse_codes[current_code]
                current_code = ""
        
        return decoded_data

# Contoh penggunaan
if __name__ == "__main__":
    huffman = HuffmanCoding()
    
    # Contoh data
    data = "hello world"
    
    # Encode
    encoded_data, codes = huffman.encode(data)
    print("Huffman Codes:", codes)
    print("Encoded Data:", encoded_data)
    
    # Decode
    decoded_data = huffman.decode(encoded_data, codes)
    print("Decoded Data:", decoded_data)