from domain.symbol_table import SymbolTable
from domain.scanner_manager import *
from domain.pif import *
from domain.finite_automaton import *


class Controller:
    def __init__(self, program_name):
        self._symbol_table = SymbolTable(19)
        self._pif = PIF()
        self._error_message = ""
        self._reserved_words = []
        self._separators = []
        self._operators = []
        self._program_name = program_name

    def read_file(self):
        with open('token.in', 'r') as f:
            f.readline()
            for i in range(10):
                separator = f.readline().strip()
                if separator == "<space>":
                    separator = " "
                self._separators.append(separator)
            for i in range(14):
                self._operators.append(f.readline().strip())
            for i in range(15):
                self._reserved_words.append(f.readline().strip())

    def run(self):
        self.read_file()
        constants_finite_automaton = FiniteAutomaton.read_from_file('constants_finite_automaton.in')
        identifiers_finite_automaton = FiniteAutomaton.read_from_file('identifiers_finite_automaton.in')

        with open(self._program_name, 'r') as file:
            line_index = 0
            for line in file:
                line_index += 1
                token_list = scan(line.strip(), self._operators, self._separators)
                sign_flag = False

                for i in range(len(token_list)):

                    # check if reserved word, operator/separator of one character
                    if token_list[i] in self._reserved_words or token_list[i] in self._separators \
                            or token_list[i] in self._operators:
                        if token_list[i] == " ":
                            continue
                        self._pif.add(token_list[i], (-1, -1))

                    elif token_list[i][:-1] in self._reserved_words or token_list[i][:-1] in self._separators \
                            or token_list[i][:-1] in self._operators:
                        if token_list[i][-1] == '-':
                            if re.match("[1-9]", token_list[i + 1]):
                                self._pif.add(token_list[i][:-1], (-1, -1))
                                sign_flag = True

                    # check if the corresponding fa accepts it as identifier
                    elif identifiers_finite_automaton.is_accepted(token_list[i]):
                        identifier_pos = self._symbol_table.insert(token_list[i])
                        self._pif.add("id", identifier_pos)

                    # check if the corresponding fa accepts it as constant
                    elif constants_finite_automaton.is_accepted(token_list[i]):

                        if sign_flag:
                            constant_pos = self._symbol_table.insert('-' + token_list[i])
                            sign_flag = False
                        else:
                            constant_pos = self._symbol_table.insert(token_list[i])
                        self._pif.add("const", constant_pos)

                    # lexical error, otherwise
                    else:
                        self._error_message += 'Lexical error at token ' + token_list[i] + ', line ' + str(
                            line_index) + "\n"

        with open('st.out', 'w') as writer:
            writer.write(str(self._symbol_table))

        with open('pif.out', 'w') as writer:
            writer.write(str(self._pif))

        if self._error_message == '':
            print("Lexically correct")
        else:
            print(self._error_message)
