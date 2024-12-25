class QuickSort():
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.sort(left) + middle + self.sort(right)

# Contoh Penggunaan
if __name__ == "__main__":
    sorter = QuickSort()
    data = [10, 7, 8, 9, 1, 5]
    print("Quick Sort:", sorter.sort(data))