class LabirintTurtle:
    def __init__(self):
        self.row = 0
        self.col = 0

    def load_map(self, name):
        self.field = open(name, 'r')
        self.line = self.field.read().split('\n')
        self.row = int(self.line[-2])
        self.col = int(self.line[-1])

    def show_map(self, turtle=False):
        for i in range(len(self.line) - 2):
            if turtle:
                f = self.line[self.row]
                self.line[self.row] = f[:self.col] + 'A' + f[self.col + 1::]
            print(self.line[i])
