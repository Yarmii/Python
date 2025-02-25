def shaker_sort(arr):
    left = 0
    right = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        
        left += 1

        for i in range(left, right + 1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        
        right -= 1

arr = [5, 3, 8, 4, 2]
print("Исходный массив:", arr)
shaker_sort(arr)
print("Отсортированный массив:", arr)