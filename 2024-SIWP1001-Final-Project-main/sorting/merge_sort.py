class MergeSort:
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self.merge(left, right)

# Contoh Penggunaan
if __name__ == "__main__":
    sorter = MergeSort()
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Merge Sort:", sorter.sort(data))
