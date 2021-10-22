import re

from domain.symbol_table import SymbolTable
from domain.scanner import Scanner
from domain.tokens_manager import *

class Main:
    def __init__(self):
        self.symbol_table = SymbolTable(19)
        self.scanner = Scanner()

    def run(self):
        readFile()
        fileName = "p1.txt"

        with open(fileName, 'r') as file:
            lineCounter = 0
            for line in file:
                lineCounter += 1
                tokens = self.scanner.scan(line.strip())
                print(tokens)

main = Main()
main.run()