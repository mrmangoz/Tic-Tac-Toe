class Symbols:
    def __init__(self):
        self.symbols = []

    def add(self, symbol):
        self.symbols.append(symbol)

    def check_loop(self, i, j):
        for i in range(3):
            for j in range(3):
                for symbol in self.symbols:
                    if symbol.pos == (i, j):
                        return(True)
                    else:
                        return(False)

    def line_check(self, symbol):
        found = 0
        if self.check_loop():
            found += 1
        #print(found)
        if found == 3:
            return("line found")
