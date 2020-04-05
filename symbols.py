class Symbols:
    def __init__(self):
        self.symbols = []

    def add(self, symbol):
        self.symbols.append(symbol)

    def line_check(self, symbol):
        found = 0
        for x in range(3):
            for y in range(3):
                for symbol in self.symbols:
                    if symbol.pos == (x, y):
                        found += 1
        #print(found)
        if found == 3:
            return("line found")
