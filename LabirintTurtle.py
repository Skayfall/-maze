class LabirintTurtle:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.turtle = False

    def load_map(self, name):
        self.field = open(name, 'r')
        self.line = self.field.read().split('\n')
        self.row = self.line[-2]
        self.col = self.line[-1]
        
    def show_map(self):
        for i in range(len(self.line) - 2):
             print(self.line[i])
