from random import randint
class TicTacToe:

    FREE_CELL = 0      # свободная клетка
    HUMAN_X = 1        # крестик (игрок - человек)
    COMPUTER_O = 2     # нолик (игрок - компьютер)  

    def __init__(self):
        self.pole = [[Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()]]
    
    def init(self):
        self.pole = [[Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()]]

    @property
    def is_human_win(self):
        p = self.pole
        if any([p[0][0].value == p[0][1].value == p[0][2].value == self.HUMAN_X,
            p[1][0].value == p[1][1].value == p[1][2].value == self.HUMAN_X,
            p[2][0].value == p[2][1].value == p[2][2].value == self.HUMAN_X,
            p[0][0].value == p[1][0].value == p[2][0].value == self.HUMAN_X,
            p[0][1].value == p[1][1].value == p[2][1].value == self.HUMAN_X,
            p[0][2].value == p[1][2].value == p[2][2].value == self.HUMAN_X,
            p[0][0].value == p[1][1].value == p[2][2].value == self.HUMAN_X,
            p[2][0].value == p[1][1].value == p[0][2].value == self.HUMAN_X]):
            return True
        return False

    @property
    def is_computer_win(self):
        p = self.pole
        if any([p[0][0].value == p[0][1].value == p[0][2].value == self.COMPUTER_O,
            p[1][0].value == p[1][1].value == p[1][2].value == self.COMPUTER_O,
            p[2][0].value == p[2][1].value == p[2][2].value == self.COMPUTER_O,
            p[0][0].value == p[1][0].value == p[2][0].value == self.COMPUTER_O,
            p[0][1].value == p[1][1].value == p[2][1].value == self.COMPUTER_O,
            p[0][2].value == p[1][2].value == p[2][2].value == self.COMPUTER_O,
            p[0][0].value == p[1][1].value == p[2][2].value == self.COMPUTER_O,
            p[2][0].value == p[1][1].value == p[0][2].value == self.COMPUTER_O]):
            return True
        return False
    
    @property
    def is_draw(self):
        if not self.is_human_win and not self.is_computer_win and not self:
            return True
        return False


    def show(self):
        for row in self.pole:
            for cell in row:
                if cell.value == self.FREE_CELL:
                    print('*', end=' ') 
                elif cell.value == self.HUMAN_X:
                    print('X', end=' ')
                else:
                    print('O', end=' ')
            print('')

    def human_go(self):
        r = int(input("Enter index for x coordinat: "))
        c = int(input("Enter index for y coordinat: "))
        self.pole[r][c].value = self.HUMAN_X

    def computer_go(self):
        while True:
            r, c = randint(0, 2), randint(0, 2)
            if self.pole[r][c]:
                self.pole[r][c].value = self.COMPUTER_O
                break
        

    @staticmethod
    def _check_indx(ind1, ind2):
        if not type(ind1) == int or not 0 <= ind1 <= 2\
            or not type(ind2) == int or not 0 <= ind2 <= 2:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, indx):
        r, c = indx
        self._check_indx(r, c)
        return self.pole[r][c].value

    def __setitem__(self, indx, value):
        r, c = indx
        self._check_indx(r, c)
        self.pole[r][c].value = value

    def __bool__(self):
        for i in self.pole:
            for j in i:
                if j.value == self.FREE_CELL:
                    return True
        return False

class Cell(TicTacToe):

    def __init__(self):
        self.value = self.FREE_CELL

    def __bool__(self):
        return not bool(self.value)


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    print()
    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")