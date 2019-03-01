from ai import AI

# play
class Player(object):
    def __init__(self, color):
        self.color = color

    # think
    def think(self, board):
        pass

    # place discs
    def move(self, board, action):
        flipped_pos = board._move(action, self.color)
        return flipped_pos

    # unmove discs
    def unmove(self, board, action, flipped_pos):
        board._unmove(action, flipped_pos, self.color)


# humanplayer
class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def think(self, board):
        while True:
            action = input("Turn to '{}'. \nPlease think carefully and input a point.(such as 'A1'): ".format(self.color))  # A1~H8
            d, e = action[1], action[0].upper()
            if d in '12345678' and e in 'ABCDEFGH':  # legality check
                x, y = '12345678'.index(d), 'ABCDEFGH'.index(e)
                if (x, y) in board.get_legal_actions(self.color):  # legality check
                    return x, y


# AI player（multiple inherit）
class AIPlayer(Player, AI):

    def __init__(self, color, level_ix=0):
        super().__init__(color)  # init Player
        super(Player, self).__init__(level_ix)  # init AI

    def think(self, board):
        print("Turn to '{}'. \nPlease wait a moment. AI is thinking...".format(self.color))
        opcolor = ['W', 'B'][self.color == 'W']
        enemy = AIPlayer(opcolor)  # hypothesized enemy
        action = self.brain(board, enemy, 2)  # Change the last number to 5 if you want to check
        return action
