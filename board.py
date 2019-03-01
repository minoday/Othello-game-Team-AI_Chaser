class Board(object):
    def __init__(self):
        self.empty = '.'
        self._board = [[self.empty for _ in range(8)] for _ in range(8)]  # size：8*8
        self._board[3][4], self._board[4][3] = 'W', 'W'
        self._board[3][3], self._board[4][4] = 'B', 'B'

    # add Board[][] index
    def __getitem__(self, index):
        return self._board[index]

    # print board
    def print_b(self):
        board = self._board
        print(' ', ' '.join(list('ABCDEFGH')))
        for i in range(8):
            print(str(i + 1), ' '.join(board[i]))

    # place discs (result is the function of flipping discs）
    def _move(self, action, color):
        x, y = action
        self._board[x][y] = color

        return self._flip(action, color)

    # place discs（back to list）
    def _flip(self, action, color):
        flipped_pos = []

        for line in self._get_lines(action):
            for i, p in enumerate(line):
                if self._board[p[0]][p[1]] == self.empty:
                    break
                elif self._board[p[0]][p[1]] == color:
                    flipped_pos.extend(line[:i])
                    break

        for p in flipped_pos:
            self._board[p[0]][p[1]] = color

        return flipped_pos

    # unmove
    def _unmove(self, action, flipped_pos, color):
        self._board[action[0]][action[1]] = self.empty

        opcolor = ['W', 'B'][color == 'W']
        for p in flipped_pos:
            self._board[p[0]][p[1]] = opcolor

    # generate subscripts in eight directions for convenience
    def _get_lines(self, action):
        board_coord = [(i, j) for i in range(8) for j in range(8)]  # board coordinate

        d, e = action
        ix = d * 8 + e
        d, e = ix // 8, ix % 8
        left = board_coord[d * 8:ix]  # flip
        right = board_coord[ix + 1:(d + 1) * 8]
        top = board_coord[e:ix:8]  # flip
        bottom = board_coord[ix + 8:8 * 8:8]

        if d <= e:
            lefttop = board_coord[e - d:ix:9]  # flip
            rightbottom = board_coord[ix + 9:(7 - (e - d)) * 8 + 7 + 1:9]
        else:
            lefttop = board_coord[(d - e) * 8:ix:9]  # flip
            rightbottom = board_coord[ix + 9:7 * 8 + (7 - (e - d)) + 1:9]

        if d + e <= 7:
            leftbottom = board_coord[ix + 7:(d + e) * 8:7]
            righttop = board_coord[d + e:ix:7]  # flip
        else:
            leftbottom = board_coord[ix + 7:7 * 8 + (d + e) - 7 + 1:7]
            righttop = board_coord[((d + e) - 7) * 8 + 7:ix:7]  # flip

        # four conditions to flip, easy to determine
        left.reverse()
        top.reverse()
        lefttop.reverse()
        righttop.reverse()
        lines = [left, top, lefttop, righttop, right, bottom, leftbottom, rightbottom]
        return lines

    # check if there are any positions to flip
    def _can_flipped(self, action, color):
        flipped_pos = []

        for line in self._get_lines(action):
            for i, p in enumerate(line):
                if self._board[p[0]][p[1]] == self.empty:
                    break
                elif self._board[p[0]][p[1]] == color:
                    flipped_pos.extend(line[:i])
                    break
        return [False, True][len(flipped_pos) > 0]

    # legal moves
    def get_legal_actions(self, color):
        opcolor = ['W', 'B'][color == 'W']
        opcolor_near_points = []  # empty squares near opposing colors

        board = self._board
        for i in range(8):
            for j in range(8):
                if board[i][j] == opcolor:
                    for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x <= 7 and 0 <= y <= 7 and board[x][y] == self.empty and (
                        x, y) not in opcolor_near_points:
                           opcolor_near_points.append((x, y))
        for p in opcolor_near_points:
            if self._can_flipped(p, color):
                yield p

    # game terminate
    def teminate(self):
        list1 = list(self.get_legal_actions('W'))
        list2 = list(self.get_legal_actions('B'))
        return [False, True][len(list1) == 0 and len(list2) == 0]

    # determine winner
    def get_winner(self):
        n1, n2 = 0, 0
        for i in range(8):
            for j in range(8):
                if self._board[i][j] == 'W':
                    n1 += 1
                if self._board[i][j] == 'B':
                    n2 += 1
        if n1 > n2:
            return 1  # B wins
        elif n1 < n2:
            return -1  # W wins
        elif n1 == n2:
            return 0  # Draw