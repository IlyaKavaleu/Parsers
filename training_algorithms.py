def search(attr, item):
    keys = list(attr.keys())
    low = 0
    high = len(keys) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_key = keys[mid]

        if mid_key == item:
            return attr[mid_key]
        elif mid_key < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


listik_1 = {9: '8', 8: '6', 7: '5', 6: '3', 5: '1', 4: '9', 3: '0', 2: '2', 1: '404', 0: '5996'}
d = dict(sorted(listik_1.items()))
print(d)
print(search(d, 9))

# s = search(listik_1, 3)  # You should search for the value, not the index
# if s is not None:
#     print(f"Value '{item}' found at index {s}.")
# else:
#     print("Value not found.")


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pinot = array[0]
#         less = [x for x in array if x < pinot]
#         more = [x for x in array if x > pinot]
#     return quicksort(less) + [pinot] + quicksort(more)
#
#
# items = [7, 4, 3, 5, 3, 0, 8, 2, 1]
# print(quicksort(items))
#
# def sel(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[min_idx], arr[i] = arr[i], arr[min_idx]
#     return arr
#
#
# my_list = [64, 25, 12, 22, 11]
# print(sel(my_list))
#
#
# def findSmallest(arr):
#     value = arr[0]
#     index_now = 0
#     for x in range(len(arr)):
#         if arr[x] < value:
#             value = arr[x]
#             index_now = x
#     return index_now
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
#
# print(selectionSort([5, 3, 6, 2, 10]))
#
#
# def a(attr):
#     dates = len(attr)
#     for x in attr:
#         for y in range(dates - 1):
#             if attr[y] > attr[y + 1]:
#                 attr[y + 1], attr[y] = attr[y], attr[y + 1]
#     return attr
# listik = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(a(listik))
#
#
# class Bubble_and_SEARCH_item:
#     def __init__(self, items):
#         self.items = items
#
#     def bubble_sorted(self):
#         """Bubble sorted"""
#         data = len(self.items)
#         for x in self.items:
#             for y in range(data - 1):
#                 if self.items[y] > self.items[y + 1]:
#                     self.items[y + 1], self.items[y] = self.items[y], self.items[y + 1]
#         return self.items
#
#     def search_item(self, attr: list, item):
#         """Search item"""
#         sorted_list = sorted(attr)
#
#         low = 0
#         high = len(sorted_list) - 1
#
#         while low <= high:
#             mid = int((low + high) / 2)
#             guess = sorted_list[mid]
#             if guess == item:
#                 return guess
#             if guess < item:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return None
#
#
# list_1 = [4, 18, 6, 2, 2, 2, 1, 4, 6, 7, 2, 0, 7, 4, 2]
# bubble = Bubble_and_SEARCH_item(list_1)
# data = bubble.bubble_sorted()
# print(data)
# print(bubble.search_item(data, 7))
#
#
#
