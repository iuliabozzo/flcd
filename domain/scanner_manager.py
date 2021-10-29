import re


def is_operator(char, operators):
    for operator in operators:
        if char in operator:
            return True
    return False


def get_operator(line, index, operators):
    token = ''

    while index < len(line) and is_operator(line[index], operators):
        token += line[index]
        index += 1

    return token, index


def get_string_token(line, index):
    token = re.findall(r'("[^"]*")', line)[0]
    index = index + len(token)

    return token, index


def scan(line, operators, separators):
    token = ''
    index = 0
    token_list = []
    while index < len(line):

        if is_operator(line[index], operators):
            if token:
                token_list.append(token)

            token, index = get_operator(line, index, operators)
            token_list.append(token)
            token = ''

        elif line[index] in separators:
            if token:
                token_list.append(token)
            token, index = line[index], index + 1
            token_list.append(token)
            token = ''

        elif line[index] == '\"':
            if token:
                token_list.append(token)
            token, index = get_string_token(line, index)
            token_list.append(token)
            token = ''

        else:
            token += line[index]
            index += 1

    if token:
        token_list.append(token)

    return token_list
