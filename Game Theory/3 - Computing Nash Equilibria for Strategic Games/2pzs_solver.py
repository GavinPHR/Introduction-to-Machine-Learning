# Solver for 2-player zero-sum game given a payoff matrix
from ortools.linear_solver import pywraplp


def minimax(payoff):
    solver = pywraplp.Solver.CreateSolver('GLOP')
    X = []
    for i in range(1, len(payoff) + 1):
        X.append(solver.NumVar(0, solver.infinity(), 'x' + str(i)))
    v = solver.NumVar(-solver.infinity(), solver.infinity(), 'v')
    for j in range(len(payoff[1])):  
        solver.Add(sum(X[i] * payoff[i][j] for i in range(len(X))) >= v)
    solver.Add(sum(X) == 1)
    solver.Maximize(v)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        for x in X:
            print(x.name, x.solution_value())
    else:
        print('The problem does not have an optimal solution.')
        
    solver = pywraplp.Solver.CreateSolver('GLOP')
    Y = []
    for j in range(1, len(payoff[0]) + 1):
        Y.append(solver.NumVar(0, solver.infinity(), 'y' + str(j)))
    u = solver.NumVar(-solver.infinity(), solver.infinity(), 'u')
    for i in range(len(payoff)):  
        solver.Add(sum(Y[j] * payoff[i][j] for j in range(len(Y))) <= u)
    solver.Add(sum(Y) == 1)
    solver.Minimize(u)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        for y in Y:
            print(y.name, y.solution_value())
    else:
        print('The problem does not have an optimal solution.')


payoff = [[1, 2, 7, 2, 4],
          [0, 0, 9, 6, 2],
          [7, 9, 4, 5, 3],
          [1, 4, 0, 7, 9],
          [9, 7, 3, 8, 3]]


minimax(payoff)
