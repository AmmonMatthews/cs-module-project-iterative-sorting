# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for m in range (cur_index +1, len(arr)):
            # print("m", arr[m])
            if arr[smallest_index] > arr[m]:
                smallest_index = m
                
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
'''
    1. Compare the first and second item of a collection. If the first item is bigger than the second item, swap the items.
    2. Move to the next item. Now, we will compare the second item with the third item. If the second item is bigger than the third, swap the items.
    3. Do this for every item until the end of the list.
    4.Repeat steps 1-3 (decrementing “the end of the list” by 1 each time).
    '''
# def bubble_sort(arr):
#     # Your code here
#     for num in range(len(arr)-1, 1, -1):
#         # print("num", num)
#         for i in range(num):
#             # print("arr[i]", arr[i])
#             # print("arr[i+1]", arr[i+1])
#             if arr[i] > arr[i+1]:
#                 temp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = temp
#             # print(arr)
#     return arr

def bubble_sort(arr):
    m = len(arr)
# Traverse through all the array elements
    for u in range(m):
        for v in range(0, m-u-1):
        # traverse the array from 0 to m-u-1
        # Swap if the element is greater than adjacent next one
            if arr[v] > arr[v+1]:
                arr[v], arr[v+1] = arr[v+1], arr[v]
    return arr


# # ALTERNATE SOLUTION
# def bubble_sort(alist):
#     for i in range(len(alist) - 1, 0, -1):
#         no_swap = True
#         for j in range(0, i):
#             if alist[j + 1] < alist[j]:
#                 alist[j], alist[j + 1] = alist[j + 1], alist[j]
#                 no_swap = False
#         if no_swap:
#             return alist


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr

print("selection sort", selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# print("bublle sort", bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))