def binary_search(a, key):
    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == key:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


a = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

result = binary_search(a, key)

if result != -1:
    print("Element found at position", result + 1)
else:
    print("Element not found")