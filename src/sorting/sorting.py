# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    arrA_l = len(arrA)
    arrB_l = len(arrB)
    i = 0
    j = 0
    k = 0

    while i < arrA_l and j < arrB_l:
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            j = j + 1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1

    while i < arrA_l:
        merged_arr[k] = arrA[i];
        k = k + 1
        i = i + 1

    while j < arrB_l:
        merged_arr[k] = arrB[j];
        k = k + 1
        j = j + 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) //2
        Left = arr[:mid]
        Right = arr[mid:]  #includes the mid index position
        merge_sort(Left)
        merge_sort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i+= 1
            else:
                arr[k] = Right[j]
                j+= 1
            k+= 1
        while i < len(Left):
            arr[k] = Left[i]
            i+= 1
            k+= 1
        while j < len(Right):
            arr[k] = Right[j]
            j+= 1
            k+= 1


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

