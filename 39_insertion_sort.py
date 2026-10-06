def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = key


a = [12, 11, 13, 5, 6]

insertion_sort(a)

print("Sorted list:", a)