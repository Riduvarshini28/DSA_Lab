import heapq

def heap_sort(arr):
    heapq.heapify(arr)   # convert list → heap
    sorted_arr = []

    while arr:
        sorted_arr.append(heapq.heappop(arr))  # remove smallest

    return sorted_arr


# 🔹 FUNCTION CALL
arr = [4, 1, 3, 2]
print(heap_sort(arr))