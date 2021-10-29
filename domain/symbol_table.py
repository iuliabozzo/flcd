from domain.hashtable import HashTable


class SymbolTable:
    def __init__(self, capacity):
        self._hashtable = HashTable(capacity)

    def insert(self, key):
        return self._hashtable.insert(key)

    def contains(self, key):
        return self._hashtable.contains(key)

    def lookup(self, key):
        return self._hashtable.lookup(key)

    def __str__(self):
        return str(self._hashtable)