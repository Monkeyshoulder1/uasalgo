class CountingSort:
    def sort(self, arr):
        max_val = max(arr)
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        sorted_arr = []
        for i, freq in enumerate(count):
            sorted_arr.extend([i] * freq)
        return sorted_arr

# Contoh Penggunaan
if __name__ == "__main__":
    sorter = CountingSort()
    data = [4, 2, 2, 8, 3, 3, 1]
    print("Counting Sort:", sorter.sort(data))
