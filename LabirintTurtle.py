from termcolor import colored

class LabirintTurtle:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.k = 0
        self.col_1 = 0
        self.row_1 = 0
        self.comp = 4
        self.len = 0
        #вверх comp = 1
        #вниз comp = 2
        #влево comp = 3
        #вправо comp = 4
        self.nap = []
        self.check = True
        self.check_1 = False
        self.check_2 = False
        self.check_3 = False

    def load_map(self, name):
        self.field = open(name, 'r')
        self.line = (self.field.read()).split('\n')
        self.row = int(self.line[-2])
        self.col = int(self.line[-1])
        self.len = len(self.line[0])


    def show_map(self, turtle=False):
        if self.check:
            for i in range(len(self.line) - 2):
                if turtle:
                    f = self.line[self.row]
                    self.line[self.row] = f[:self.col] + '\u2698' + f[self.col + 1::]
                print(colored(self.line[i], 'magenta'))

    def check_map(self):
        for i in self.line[:-2]:
            for j in i:
                if j == '*' or j == ' ' or j == '\u2698':
                    self.k += 1
        if self.k == (len(self.line) - 2) * self.len:
            self.check_1 = True

        for i in range(len(self.line) - 2):
            if 0 < self.row < self.len - 1:
                if 0 < self.col < self.len - 1:
                    if self.line[self.row][self.col] != '*':
                        self.check_2 = True

        for i in self.line[0][1:-1]:
            if i == ' ' and self.line[0][0] != ' ' and self.line[0][-1] != ' ':
                self.col_1 = self.line[0][1:-1].index(i) + 1
                self.row_1 = 0
                self.check_3 = True
        for i in self.line[:-2][-1][1:-1]:
            if i == ' ' and self.line[:-2][-1][0] != ' ' and self.line[:-2][-1][-1] != ' ':
                self.col_1 = self.line[:-2][-1][1:-1].index(i) + 1
                self.row_1 = len(self.line) - 2
                self.check_3 = True
        for i in self.line[1:-3]:
            for j in i:
                if j[0] == ' ' or j[-1] == ' ':
                    self.check_3 = True
        if self.row_1 == 0 and self.col_1 == 0:
            self.check_3 = False

        if not self.check_1 or not self.check_2 or not self.check_3:
            self.check = False
            print('Карта невалидна, пожалуйста загрузите новую карту.')

    def exit_count_step(self):
        print(self.row, self.col)
        print(self.row_1, self.col_1)
        print('-----------------')

    def exit_show_step(self):
        while self.line[self.row][self.col + 1] != '*':
            self.col += 1
            self.nap.append('E')
            f = self.line[self.row]
            self.line[self.row] = f[:self.col] + '\u2022' + f[self.col + 1::]

        while self.row != self.row_1 and self.col != self.col_1:
            if self.comp == 1:
                self.up()
                print(self.row, self.col)
                print(self.row_1, self.col_1)
                print('-----------------')
            elif self.comp == 2:
                self.down()
                print(self.row, self.col)
                print(self.row_1, self.col_1)
                print('-----------------')
            elif self.comp == 3:
                self.left()
                print(self.row, self.col)
                print(self.row_1, self.col_1)
                print('-----------------')
            elif self.comp == 4:
                self.right()
                print(self.row, self.col)
                print(self.row_1, self.col_1)
                print('-----------------')
        if self.row_1 == 0:
            self.row -= 1
            self.nap.append('N')
            f = self.line[self.row]
            self.line[self.row] = f[:self.col] + '\u2698' + f[self.col + 1::]
        elif self.row_1 == len(self.line) - 2:
            self.row += 1
            self.nap.append('S')
            f = self.line[self.row]
            self.line[self.row] = f[:self.col] + '\u2698' + f[self.col + 1::]

        self.nap.remove('N')
        self.nap.remove('E')
        print(self.nap)

    def up(self):
        self.comp = 1
        if self.line[self.row - 1][self.col] == '*':
            self.row += 1
            self.comp = 3
        elif self.line[self.row - 1][self.col + 1] == ' ':
            self.comp = 4
        self.row -= 1
        self.nap.append('N')
        f = self.line[self.row]
        self.line[self.row] = f[:self.col] + '\u2022' + f[self.col + 1::]

    def down(self):
        self.comp = 2
        if self.line[self.row + 1][self.col] == '*':
            self.row -= 1
            self.comp = 4
        elif self.line[self.row + 1][self.col - 1] == ' ':
            self.comp = 3
        self.row += 1
        self.nap.append('S')
        f = self.line[self.row]
        self.line[self.row] = f[:self.col] + '\u2022' + f[self.col + 1::]

    def left(self):
        self.comp = 3
        if self.line[self.row][self.col - 1] == '*':
            self.col += 1
            self.comp = 2
        elif self.line[self.row - 1][self.col - 1] == ' ':
            self.comp = 1
        self.col -= 1
        self.nap.append('W')
        f = self.line[self.row]
        self.line[self.row] = f[:self.col] + '\u2022' + f[self.col + 1::]

    def right(self):
        self.comp = 4
        if self.line[self.row][self.col + 1] == '*':
            self.col -= 1
            self.comp = 1
        elif self.line[self.row + 1][self.col + 1] == ' ':
            self.comp = 2
        self.col += 1
        self.nap.append('E')
        f = self.line[self.row]
        self.line[self.row] = f[:self.col] + '\u2022' + f[self.col + 1::]
