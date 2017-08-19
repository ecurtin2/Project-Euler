import copy
import random
import collections

with open('96.dat') as f:
    puzzles = f.readlines()

grids = {}
key = 'blank'
for line in puzzles:
    if 'Grid' in line:
        key = line.split(' ')[1].replace('\n', '')
        grids[key] = []
        count = 0
    else:
        grids[key].append(line.replace('\n', ''))

grids = {k: [[int(i) for i in s] for s in v] for k, v in grids.items()}

grid = grids['01']


class SubContainer(object):
    def __init__(self, sudoku_puzzle, squares, identity=None):
        self.squares = squares
        self.identity = identity
        for square in squares:
            square.add_subcontainer(self, identity)
        self.sudoku_puzzle = sudoku_puzzle
        self.idx = None

    def __str__(self):
        l = ["Subcontainer of type {} and location {}".format(self.identity, str(self.idx))]
        l += ["With the following values: {}".format([square.value for square in self.squares])]
        return ' '.join(l)

    @property
    def is_solved(self):
        return all(i.is_solved for i in self.squares)

    @property
    def contains(self):
        return [square.value for square in self.squares]

    @property
    def requires(self):
        return set(i for i in range(1, 10) if i not in self.contains)

    def solve_obvious(self):
        if not self.is_solved:
            if len(self.requires) == 1:
                val = self.requires.pop()
                unsolved_squares = [square for square in self.squares if not square.is_solved]
                if len(unsolved_squares) != 1:
                    raise AttributeError('Subcontainer has a required value but no unsolved squares!: \n'
                                         + self.__str__())
                else:
                    square = unsolved_squares[0]
                    square.value = val


class SudokuPuzzle(object):

    class Square(object):

        def __init__(self, global_row_idx, global_col_idx, value):
            self.global_row_idx = global_row_idx
            self.global_col_idx = global_col_idx
            self.value = value
            self.subcontainers = {}

        def add_subcontainer(self, instance, identity):
            self.subcontainers[identity] = instance

        @property
        def candidates(self):
            if self.is_solved:
                return set()
            else:
                prohibited = set.union(*[set(container.contains) for container in self.subcontainers.values()])
                return {i for i in range(1, 10) if i not in prohibited}

        @property
        def is_solved(self):
            return self.value != 0

        def __str__(self):
            l = ['Square at location {i}, {j} with value {v}'.format(i=self.global_row_idx,
                                                                     j=self.global_col_idx,
                                                                     v=self.value)]

            return ''.join(l)

        def guess(self):
            if not self.is_solved:
                if len(self.candidates) == 0:
                    raise AttributeError("Puzzle is In unsolvable state!")
                self.value = random.choice(list(self.candidates))

        def solve_obvious(self):
            if not self.is_solved:
                if len(self.candidates) == 1:
                    self.value = self.candidates.pop()

    class Box(SubContainer):

        def __init__(self, sudoku_puzzle, global_i, global_j):
            squares = [sudoku_puzzle.squares[3*global_i + i][3*global_j + j] for i in range(3) for j in range(3)]
            super().__init__(sudoku_puzzle, squares, identity='Box')
            self.idx = (global_i, global_j)

    class Row(SubContainer):
        def __init__(self, sudoku_puzzle, idx):
            row = [sudoku_puzzle.squares[idx][j] for j in range(9)]
            super().__init__(sudoku_puzzle, row, identity='Row')
            self.idx = idx

    class Col(SubContainer):
        def __init__(self, sudoku_puzzle, idx):
            col = [sudoku_puzzle.squares[j][idx] for j in range(9)]
            super().__init__(sudoku_puzzle, col, identity='Col')
            self.idx = idx

    def __init__(self, grid, identity='Unnamed'):
        self.identity = identity
        self.squares = [[__class__.Square(i, j, grid[i][j]) for i in range(9)] for j in range(9)]
        self.allsquares = [square for row in self.squares for square in row]
        self.rows = [__class__.Row(self, i) for i in range(9)]
        self.cols = [__class__.Col(self, i) for i in range(9)]
        self.boxes = [__class__.Box(self, i, j) for i in range(3) for j in range(3)]
        self.containers = self.rows + self.cols + self.boxes
        self.original_str = self.get_list_str()
        self.iterations = 0
        self.save_states = {}
        self.invalid_containers = []
        self.combo_its = 0
        self.obvious_its = 0
        self.guess_its = 0

    @property
    def is_solved(self):
        return all(square.is_solved for square in self.allsquares) and self.is_valid

    @property
    def is_valid(self):
        self.invalid_containers = []
        for cont in self.containers:
            counter = collections.Counter(cont.contains)
            if any(val > 1 for val in counter.values()):
                self.invalid_containers.append(cont)
                return False
            else:
                return True

    def solve_combo(self, maxits=10):

        count = 0
        while not puzzle.is_solved:
            self.combo_its += 1
            count += 1
            if count >= maxits:
                return None
            self.save('first')
            self.solve_obvious()
            if not puzzle.is_solved:
                puzzle.attempt_solve_by_guess(10)
            if not puzzle.is_solved:
                puzzle.load('first')

    def solve_obvious(self, max_iters=10):
        count = 0
        while not self.is_solved:
            self.obvious_its += 1
            old_vals = copy.copy([square.value for square in self.allsquares])
            count += 1
            for square in self.allsquares:
                square.solve_obvious()
            for cont in self.containers:
                cont.solve_obvious()
            if count == max_iters:
                break
            if old_vals == [square.value for square in self.allsquares]:
                break
        self.iterations = count

    def save(self, key):
        self.save_states[key] = {square: square.value for square in self.allsquares}

    def load(self, key):
        for square in self.allsquares:
            square.value = self.save_states[key][square]

    def attempt_solve_by_guess(self, maxits=10):

        count = 0
        self.save('hard')
        while not puzzle.is_solved:
            self.guess_its += 1
            self.save('soft')
            count += 1
            try:
                choices = [square for square in self.allsquares if not square.is_solved]
                square = random.choice(choices)
                square.guess()
                self.solve_obvious(max_iters=10)
            except AttributeError: # Raises attributerror if unsolvable, reset to savepoint.
                self.load('soft')
            except IndexError:
                self.load('soft')
            if count == maxits:
                break

    def get_list_str(self):
        l = []
        for i, row in enumerate(self.squares):
            s = ' '.join([str(square.value) for square in row]).replace('0', ' ')
            s = s[:5] + ' |' + s[5:11] + ' |' + s[11:]
            l.append(s)
            if (i+1) % 3 == 0:
                l.append('-'*(len(s)+2))
        l.pop(-1)
        return l

    def __str__(self):
        d = {True: "Solved", False: "Unsolved"}
        top = [3 * ' ' + " Sudoku: {name}   Status: {solved}   ".format(
            name=self.identity, solved=d[self.is_solved], its=self.iterations)]
        second = ['# Iterations:   Combo = {c}, Guess = {g}, Obvious = {o}'.format(
            c=self.combo_its, g=self.guess_its, o=self.obvious_its)]
        third = [' '*9 + 'Original' + ' '*21 + 'Current']
        l = [s1 + ' |    | ' + s2 for s1, s2 in zip(self.original_str, self.get_list_str())]
        l = ['| ' + s + ' |' for s in l]
        l = [s.replace('| -', '|-').replace('- |', '-|') if '-' in s else s for s in l]
        hline = '-' * 25 + '    ' + '-'*25
        l.append(hline)
        l = top + second + third + [hline]+ l
        return '\n' + '\n'.join(l)


puzzles = [SudokuPuzzle(v, k) for k, v in grids.items()]
max = 100

total = 0
for puzzle in puzzles:
    puzzle.solve_combo()
    num = ''.join([str(square.value) for square in puzzle.squares[0][:3]])
    total += int(num)
    print(int(num))
    print(puzzle)


print(total)

frac = sum(1 for puzzle in puzzles if puzzle.is_solved) / len(puzzles)

print("Solved {}% of Puzzles!".format(100.0*frac))