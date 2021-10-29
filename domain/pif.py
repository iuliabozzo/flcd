class PIF:
    def __init__(self):
        self._content = []

    def add(self, token, index):
        self._content.append((token, index))

    def __str__(self):
        result = ""
        for pair in self._content:
            result += pair[0] + "------" + str(pair[1]) + "\n"
        return result
