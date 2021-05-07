from tic_tac_toe import TicTacToe


class AlphaBeta:
    def __init__(self, game):
        self.game = game
        self.moves = dict()
        
    def search(self):
        v = self.max_value(-float('inf'), float('inf'))
        return v
    
    def max_value(self, alpha, beta):
        if (s := self.game.check_status()) != -1:
            return self.utility(s)
        v = -float('inf')
        move = None
        for i, j in self.game.available():
            self.game.move(i, j)
            if (minval := self.min_value(alpha, beta)) > v:
                v = minval
                move = (i, j)
            self.game.revert(i, j)
            if v >= beta:
                self.moves[hash(self.game)] = (i, j)
                return v
            alpha = max(alpha, v)
        self.moves[hash(self.game)] = move
        return v
        
    def min_value(self, alpha, beta):
        if (s := self.game.check_status()) != -1:
            return self.utility(s)
        v = float('inf')
        move = None
        for i, j in self.game.available():
            self.game.move(i, j)
            if (maxval := self.max_value(alpha, beta)) < v:
                v = maxval
                move = (i, j)
            self.game.revert(i, j)
            if v <= alpha:
                self.moves[hash(self.game)] = (i, j)
                return v
            beta = min(beta, v)
        self.moves[hash(self.game)] = move
        return v
    
    @staticmethod
    def utility(result):
        """In respect to player 1"""
        if result == 0: return 0
        if result == 1: return 1
        return -1


game = TicTacToe()
ab = AlphaBeta(game)
ab.search()
game.clear()
while (h := hash(game)) in ab.moves:
    game.move(*ab.moves[h])
    print(game)
