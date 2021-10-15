class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity
        self._items = [list() for _ in range(capacity)]

    def hash(self, value):
        sum = 0
        for c in value:
            sum += ord(c) - ord('0')
        return sum % self._capacity

    def contains(self, value):
        return value in self._items[self.hash(value)]

    def lookup(self, value):
        key_index = self.hash(value)
        value_index = 0
        for v in self._items[key_index]:
            if v != value:
                value_index += 1
            else:
                break
        return key_index, value_index

    def insert(self, value):
        if self.contains(value):
            return self.lookup(value)
        self._items[self.hash(value)].append(value)
        return self.lookup(value)

    def __str__(self):
        result = "Symbol Table\n"
        for i in range(self._capacity):
            result = result + str(i) + "->" + str(self._items[i]) + "\n"
        return result
