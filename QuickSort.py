def quickSort(numbers, begin, end):
    if begin < end:
        pivot = patrion(numbers, begin, end)

        quickSort(numbers, begin, pivot-1)

        quickSort(numbers, pivot+1, end)



def patrion(numbers, begin, end):
    # choose pivot
    pivot = arr[end]
    i = begin-1

    for j in range(begin, end):
        if numbers[j] <= pivot:
            i += 1
            swap(numbers, i, j)

    swap(numbers, i+1, end)

    return i+1

def swap(numbers, A, B):

    temp = numbers[A]
    numbers[A] = numbers[B]
    numbers[B] = temp


arr = [8,0,4,2,1,3]
quickSort(arr, 0, len(arr)-1)
print(arr)