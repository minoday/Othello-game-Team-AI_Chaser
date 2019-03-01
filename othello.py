from board import Board
from player import HumanPlayer, AIPlayer
import time

# game
class Game(object):
    def __init__(self):
        self.board = Board()
        self.current_player = None

    # create two player
    def make_two_players(self):

        player1 = AIPlayer('W')
        player2 = AIPlayer('B')


        return player1, player2

    # shift the player （in the process of the game）
    def switch_player(self, player1, player2):
        if self.current_player is None:
            return player1
        else:
            return [player1, player2][self.current_player == player1]

    # print winner
    def print_winner(self, winner):  # winner in [1,-1,0]
        print(['Winner is Black', 'Winner is White', 'Draw'][winner])

    # run the game
    def run(self):
        # create two player
        player1, player2 = self.make_two_players()

        # start the game
        print('\nGame start!\n')
        self.board.print_b()  # print the board
        while True:
            self.current_player = self.switch_player(player1, player2)  # shift to the current player

            action = self.current_player.think(self.board)  # current player is thinking then get the action，

            if action is not None:
                self.current_player.move(self.board, action)  # current player take action then change the board，

            self.board.print_b()  # print current board

            if self.board.teminate():  # determine whether to end the game based on the current board
                winner = self.board.get_winner()  # get the winner 1,-1,0
                break

        self.print_winner(winner)
        print('Game over!')


if __name__ == '__main__':
    start = time.time()
    Game().run()
    end = time.time()
    print('running time='+str((end - start) / 10))