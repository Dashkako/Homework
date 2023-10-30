#Задача 1
class Stack:
    def __init__(self):
        self.cases = []

    def push(self, case):
        self.cases.append(case)

    def pop(self):
        if not self.is_null():
            self.cases.pop()

    def is_null(self):
        return len(self.cases) == 0

class TaskManager:
    def __init__(self):
        self.task_stack = Stack()

    def tasks(self, task, priority):
        self.task_stack.push((task, priority))
        self.sorted_stack()

    def get_priority(self, task):
        return task[1]

    def sorted_stack(self):
        if self.task_stack.is_null():
            print("Стек пустой. Сортировка невозможна")
            return
        new_task = sorted(self.task_stack.cases, key=self.get_priority)
        self.task_stack.cases = new_task
    def __str__(self):
        return f"Приоритет {self.task_stack.cases}"

    def pop(self):
        self.task_stack.pop()


manager = TaskManager()
manager.tasks("сделать уборку", 4)
manager.tasks("помыть посуду", 4)
manager.tasks("отдохнуть", 1)
manager.tasks("поесть", 2)
manager.tasks("сдать дз", 2)
print(manager)
manager.pop()
print(manager)

#Задача 2
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = {}
        self.keys = []

    @property
    def cache(self):
        if not self.keys:
            return "Кеш пустой"
        old_key = self.keys[0]
        return self.items.get(old_key)

    @cache.setter
    def cache(self, new_elem):
        if len(self.items) >= self.capacity:
           del_key = self.keys.pop(0)
           del self.items[del_key]
        key, value = new_elem
        self.items[key] = value
        self.keys.append(key)

    def get(self, key):
        if not key in self.keys:
            return "Такого ключа нет"
        return self.items[key]

    def print_cache(self):
        for key in self.keys:
            print(f'{key}: {self.items[key]}')

#Задача 3
def decorator_cache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def fibonachi(n):
    if n <= 1:
        return n
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)

#Задача 4
class Cell:
    def __init__(self):
        self.is_occupied = False
        self.symbol = ' '


class Board:
    def __init__(self):
        self.cells = [Cell() for _ in range(9)]

    def display(self):
        for i in range(0, 9, 3):
            row = [self.cells[i].symbol, self.cells[i + 1].symbol, self.cells[i + 2].symbol]
            print(' | '.join(row))
            if i < 6:
                print('---------')

    def make_move(self, cell_number, symbol):
        if 1 <= cell_number <= 9 and not self.cells[cell_number - 1].is_occupied:
            self.cells[cell_number - 1].is_occupied = True
            self.cells[cell_number - 1].symbol = symbol
            return True
        return False

    def is_full(self):
        return all(cell.is_occupied for cell in self.cells)

    def check_winner(self,symbol):
        winning_combinations = [
            [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]
        ]
        for combo in winning_combinations:
            #[TRue,True,True]
            if all(self.cells[i].symbol == symbol for i in combo):
                return True
            return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                cell_number = int(input(f'{self.name} введите номер ячейки (1-9): '))
                if board.make_move(cell_number, self.symbol):
                    break
                else:
                    print("Неправильный ход,Попробуйте снова")
            except ValueError:
                print("Неправильное значение.Пожалуйста введите число от 1 до 9")


def play_game():
    board = Board()
    player1 = Player('Dasha', 'X')
    player2 = Player('Juli','O')
    current_player = player1

    while True:
        board.display()
        current_player.make_move(board)
        if board.check_winner(current_player.symbol):
            board.display()
            print(f'{current_player.name} выйграл')
            break
        elif board.is_full():
            board.display()
            print("Ничья")
            break

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

if __name__ == "__main__":
    play_game()
