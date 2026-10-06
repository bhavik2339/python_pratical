def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


a = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

result = linear_search(a, key)

if result != -1:
    print("Element found at position", result + 1)
else:
    print("Element not found")