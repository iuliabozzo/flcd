from domain.tokens_manager import *


class Scanner:

    def is_operator(self, char):
        for operator in operators:
            if char in operator:
                return True
        return False

    def get_operator(self, line, index):
        token = ''

        while index < len(line) and self.is_operator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def scan(self, line):
        current_token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_operator(line[index]):
                if current_token:
                    tokens.append(current_token)
                current_token, index = self.get_operator(line, index)
                tokens.append(current_token)
                current_token = ''

            elif line[index] in separators:
                if current_token:
                    tokens.append(current_token)
                current_token, index = line[index], index + 1
                tokens.append(current_token)
                current_token = ''

            else:
                current_token += line[index]
                index += 1
        if current_token:
            tokens.append(current_token)

        return tokens

