"""
Input c, A, b

Maximize c^T x

Subject to: Ax <= b, x >= 0
"""

class LP:
    def __init__(self, c, A, b):
        """
        Standardize
        """
        n = len(c)
        m = len(A)
        for i, a in enumerate(A):
            a += [0] * (m + 1)
            a[n + i] = 1
            a[-1] = b[i]
            if a[-1] < 0:
                for i in range(len(a)):
                    a[i] = -a[i]
        c += [0] * (m + 1)
        A.append(list(map(lambda x: -x, c)))
        self.tableau = A
        self.basis = list(range(n, n + m + 1))
        self.basis[-1] = float('nan')
        
    def pivot(self):
        """
        Find the pivot
        """
        min_val = float('inf')
        min_var = None
        for j, val in enumerate(self.tableau[-1]):
            if val < min_val:
                min_val = val
                min_var = j
        if min_val >= 0:
            print('Optimal achieved: optimal =', self.tableau[-1][-1])
            self.print()
            return
        entering = min_var
        
        min_val = float('inf')
        min_var = None
        for i, row in enumerate(self.tableau[:-1]):
            if row[entering] <= 0:
                continue
            v = row[-1] / row[entering]
            if v < min_val and v >= 0:
                min_val = v
                min_var = i
        if min_var is None:
            print('Unbounded')
            return
        leaving = min_var
        
        self._pivot(leaving, entering)
        
    def _pivot(self, leaving, entering):
        """
        Pivot with Gaussian elimination
        """
        length = len(self.tableau[0])
        divider = self.tableau[leaving][entering]
        for j in range(length):
            self.tableau[leaving][j] /= divider
        for i, row in enumerate(self.tableau):
            if i == leaving: 
                continue
            multiplier = self.tableau[i][entering]
            for j in range(length):
                self.tableau[i][j] -= multiplier * self.tableau[leaving][j]
        self.basis[leaving] = entering
        self.print()
        
    def print(self):
        for i, row in enumerate(self.tableau):
            print(row, '[' + str(self.basis[i]) + ']')
        print()

# Feasible
c = [4, 6]
A = [[-1, 1], 
     [ 1, 1],
     [ 2, 5]]
b = [11, 27, 90]

# Unbounded
# c = [1, 2]
# A = [[ 1, -3], 
#      [-1,  2]]
# b = [1, 4]

p = LP(c, A, b)

p.print()
p.pivot()
p.pivot()
p.pivot()
p.pivot()
"""
On last pivot:
Optimal achieved: optimal = 132.0
[0.0, 1.0, 0.0, -0.6666666666666665, 0.3333333333333333, 12.0] [1]
[0.0, 0.0, 1.0, 2.333333333333333, -0.6666666666666666, 13.999999999999998] [2]
[1.0, 0.0, 0.0, 1.6666666666666665, -0.3333333333333333, 14.999999999999998] [0]
[0.0, 0.0, 0.0, 2.6666666666666674, 0.6666666666666663, 132.0] [nan]
with x_0 = 15, x_1 = 12
"""