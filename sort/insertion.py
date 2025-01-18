def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def insertion_sort(arr):
    steps = []  # 用于记录排序过程
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        steps.append(arr[:])  # 记录当前排序结果
    return steps  # 返回排序过程

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

arr = [122, 341, 133, 3423, 45]

print("Original array: ")
print_arr(arr)

steps = insertion_sort(arr)  # 获取排序过程

print("Sorting process:")
for step in steps:
    print_arr(step)

print("Sorted array:")
print_arr(arr)
