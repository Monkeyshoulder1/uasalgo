class EuclideanAlgorithm:
    """
    Implementasi Algoritma Euclidean untuk mencari FPB
    """

    def gcd_recursive(self, a, b):
        """
        Metode rekursif untuk mencari FPB
        
        Args:
            a (int): Bilangan pertama
            b (int): Bilangan kedua
        
        Returns:
            int: Faktor Persekutuan Terbesar (FPB)
        """
        # Basis rekursi
        if b == 0:
            return abs(a)
        
        # Rekursi dengan modulo
        return self.gcd_recursive(b, a % b)

    def gcd_iterative(self, a, b):
        """
        Metode iteratif untuk mencari FPB
        
        Args:
            a (int): Bilangan pertama
            b (int): Bilangan kedua
        
        Returns:
            int: Faktor Persekutuan Terbesar (FPB)
        """
        # Gunakan nilai absolut
        a, b = abs(a), abs(b)
        
        # Algoritma Euclidean iteratif
        while b:
            a, b = b, a % b
        
        return a

    def extended_gcd(self, a, b):
        """
        Algoritma Euclidean Extended
        Mencari FPB dan koefisien Bezout
        
        Args:
            a (int): Bilangan pertama
            b (int): Bilangan kedua
        
        Returns:
            tuple: (FPB, x, y) dimana ax + by = gcd
        """
        # Basis rekursi
        if a == 0:
            return (b, 0, 1)
        
        # Rekursi
        gcd, x1, y1 = self.extended_gcd(b % a, a)
        
        # Hitung koefisien
        x = y1 - (b // a) * x1
        y = x1
        
        return (gcd, x, y)

    def lcm(self, a, b):
        """
        Mencari Kelipatan Persekutuan Terkecil (KPK)
        
        Args:
            a (int): Bilangan pertama
            b (int): Bilangan kedua
        
        Returns:
            int: Kelipatan Persekutuan Terkecil
        """
        return abs(a * b) // self.gcd_iterative(a, b)

# Contoh penggunaan
if __name__ == "__main__":
    euclidean = EuclideanAlgorithm()
    
    # Contoh FPB
    a, b = 48, 18
    print(f"GCD (Rekursif): {euclidean.gcd_recursive(a, b)}")
    print(f"GCD (Iteratif): {euclidean.gcd_iterative(a, b)}")
    
    # Contoh Extended GCD
    gcd, x, y = euclidean.extended_gcd(a, b)
    print(f"Extended GCD: {gcd}")
    print(f"Koefisien: x = {x}, y = {y}")
    
    # Contoh KPK
    print(f"LCM: {euclidean.lcm(a, b)}")