class TicTacToe:
    def __init__(self):
        self.next = 1
        self.grid = [[-1] * 3 for _ in range(3)]
        
    def move(self, i, j):
        if self.grid[i][j] == -1:
            self.grid[i][j] = self.next
            self.next = 2 if self.next == 1 else 1
        else:
            raise RuntimeError('Illegal spot')
        return self
    
    def revert(self, i, j):
        self.grid[i][j] = -1
        return self
            
    def available(self):
        res = []
        for i, row in enumerate(self.grid):
            for j, v in enumerate(row):
                if v == -1:
                    res.append((i, j))
        return res
    
    def check_status(self):
        """
        -1 -> not finished
         0 -> draw
         1 -> player 1 wins
         2 -> player 2 wins
        """
        g = self.grid
        for i in range(3):
            if g[i][0] == g[i][1] == g[i][2]:
                if g[i][0] != -1: return g[i][0]
            if g[0][i] == g[1][i] == g[2][i]:
                if g[0][i] != -1: return g[0][i]
        if g[0][0] == g[1][1] == g[2][2]:
            if g[0][0] != -1: return g[0][0]
        if g[0][2] == g[1][1] == g[2][0]:
            if g[0][2] != -1: return g[0][2]
        for row in g:
            for v in row:
                if v == -1: return -1
        return 0
    
    def clear(self):
        self.__init__()
        
    def __hash__(self):
        h = 0
        for row in self.grid:
            for v in row:
                h <<= 2
                if v == 1:
                    h |= 1
                elif v == 2:
                    h |= 2
        return h
    
    @staticmethod
    def from_hash(h):
        game = TicTacToe()
        g = game.grid
        i = 8
        while i != -1:
            g[8 // 3][8 % 3] = h & 3
            i -= 1
        return game
        
    def __repr__(self):
        s = ['Player 1 = X/Player 2 = O\n', '---\n']
        for i, row in enumerate(self.grid):
            for j, v in enumerate(row):
                if v == -1:
                    s.append(' ')
                elif v == 1:
                    s.append('X')
                else:
                    s.append('O')
            s.append('\n')
        s.append('---\n')
        return ''.join(s)
