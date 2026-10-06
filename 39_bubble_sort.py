def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = [64, 34, 25, 12, 22]

bubble_sort(a)

print("Sorted list:", a)