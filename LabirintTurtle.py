from termcolor import colored

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
            if turtle and self.line[self.row][self.col] != '*':
                if 0 < self.row < len(self.line[0]) - 1:
                    if 0 < self.col < len(self.line[0]) - 1:
                        f = self.line[self.row]
                        self.line[self.row] = f[:self.col] + 'A' + f[self.col + 1::]
            print(colored(self.line[i], 'magenta'))
