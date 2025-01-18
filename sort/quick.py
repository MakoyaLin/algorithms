#把比pivot小的换到左边，比pivot大的换到右边
import random


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_recursive(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        quick_sort_recursive(arr, low, mid - 1)
        quick_sort_recursive(arr, mid + 1, high)
        
def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr) - 1)
    
arr = [random.randint(1, 1000) for _ in range(100)]
print("Original array: ")
print_arr(arr)
quick_sort(arr)
print("Sorted array:")
print_arr(arr)
