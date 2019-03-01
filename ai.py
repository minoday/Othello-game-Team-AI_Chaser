class AI(object):
    '''
    two player levels：novice、master
    '''

    def __init__(self, level_ix=0):
        # player level
        self.level = ['novice', 'master'][level_ix]
        # weights of board，reference：https://github.com/k-time/ai-minimax-agent/blob/master/ksx2101.py
        self.board_weights = [
            [120, -20, 20, 5, 5, 20, -20, 120],
            [-20, -40, -5, -5, -5, -5, -40, -20],
            [20, -5, 15, 3, 3, 15, -5, 20],
            [5, -5, 3, 3, 3, 3, -5, 5],
            [5, -5, 3, 3, 3, 3, -5, 5],
            [20, -5, 15, 3, 3, 15, -5, 20],
            [-20, -40, -5, -5, -5, -5, -40, -20],
            [120, -20, 20, 5, 5, 20, -20, 120]
        ]

    # weights function（based on positions on board only）
    def evaluate(self, board, color):
        opcolor = ['W', 'B'][color == 'W']
        value = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == color:
                    value += self.board_weights[i][j]
                elif board[i][j] == opcolor:
                    value -= self.board_weights[i][j]
        return value

    # AI brain
    def brain(self, board, opponent, depth):
        if self.level == 'novice':  # novice level
            _, action = self.minimax(board, opponent, depth)
        elif self.level == 'master':  # master level
            _, action = self.minimax_alpha_beta(board, opponent, depth)
        return action

    # minimax algorithm，limit depth
    def minimax(self, board, enemy, depth=4):  # note that enemy is the hypothesized opponent
        '''reference：https://github.com/k-time/ai-minimax-agent/blob/master/ksx2101.py'''
        color = self.color

        if depth == 0:
            return self.evaluate(board, color), None

        action_list = list(board.get_legal_actions(color))
        if not action_list:
            return self.evaluate(board, color), None

        best_value = -100000
        best_action = None

        for action in action_list:
            flipped_pos = self.move(board, action)  # move
            value, _ = enemy.minimax(board, self, depth - 1)  # depth first，turn to enemy
            self.unmove(board, action, flipped_pos)  # unmove

            value = -value
            if value > best_value:
                best_value = value
                best_action = action

        return best_value, best_action

    # minimax，with alpha-beta pruning
    def minimax_alpha_beta(self, board, enemy, depth=8, my_best=-float('inf'), opp_best=float('inf')):
        '''reference：https://github.com/k-time/ai-minimax-agent/blob/master/ksx2101.py'''
        color = self.color

        if depth == 0:
            return self.evaluate(board, color), None

        action_list = list(board.get_legal_actions(color))
        if not action_list:
            return self.evaluate(board, color), None

        best_value = my_best
        best_action = None

        for action in action_list:
            flipped_pos = self.move(board, action)  # move
            value, _ = enemy.minimax_alpha_beta(board, self, depth - 1, -opp_best, -best_value)  # depth-first turn to enemy
            self.unmove(board, action, flipped_pos)  # unmove

            value = -value
            if value > best_value:
                best_value = value
                best_action = action

            if best_value > opp_best:
                break

        return best_value, best_action