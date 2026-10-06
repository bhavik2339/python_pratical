def selection_sort(a):
    for i in range(len(a)):
        min_pos = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_pos]:
                min_pos = j

        a[i], a[min_pos] = a[min_pos], a[i]


a = [64, 25, 12, 22, 11]

selection_sort(a)

print("Sorted list:", a)