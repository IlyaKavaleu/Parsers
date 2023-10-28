class Bubble_and_SEARCH_item:
    def __init__(self, items):
        self.items = items

    def bubble_sorted(self):
        data = len(self.items)
        for x in self.items:
            for y in range(data - 1):
                if self.items[y] > self.items[y + 1]:
                    self.items[y + 1], self.items[y] = self.items[y], self.items[y + 1]
        return self.items

    def search_item(self, attr: list, item):
        sorted_list = sorted(attr)

        low = 0
        high = len(sorted_list) - 1

        count = 0
        while low <= high:
            mid = int((low + high) / 2)
            guess = sorted_list[mid]
            if guess == item:
                return guess
            if guess < item:
                low = mid + 1
            else:
                high = mid - 1
        return None


list_1 = [4, 18, 6, 2, 2, 2, 1, 4, 6, 7, 2, 0, 7, 4, 2]
bubble = Bubble_and_SEARCH_item(list_1)
data = bubble.bubble_sorted()
print(data)
print(bubble.search_item(data, 7))



