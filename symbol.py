class Symbol:
    def __init__(self):
        self.pos = None
        self.type = "X"

    def add(self, pos):
        self.pos = pos

    def switch(self):
        if self.type == "X":
            self.type = "O"
        else:
            self.type = "X"
