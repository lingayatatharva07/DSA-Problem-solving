# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i] 
#         j = i - 1
#         while j >= 0 and arr[j] > key :
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# Given_array = [5, 3, 8, 6, 2]
# sorted_array = insertion_sort(Given_array)
# print("Sorted Array:", sorted_array)