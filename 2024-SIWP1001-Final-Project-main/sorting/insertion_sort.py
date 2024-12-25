class InsertionSort:
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

# Contoh Penggunaan
if __name__ == "__main__":
    sorter = InsertionSort()
    data = [5, 2, 9, 1, 5, 6]
    print("Insertion Sort:", sorter.sort(data))
