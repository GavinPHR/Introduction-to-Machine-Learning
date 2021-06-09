import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Find x that minimizes:
# f(x) = 1/2 ||Ax - b||

# Arbitrary A and b
A = np.array([[1, 2], [2, -1]])
b = [-1, 2]

def f(x):
    tmp = A.dot(x) - b
    tmp = tmp.dot(tmp)
    return tmp / 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-10, 10, 0.1)
Y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.empty(X.shape)
for i, row in enumerate(X):
    for j, x in enumerate(row):
        Z[i, j] = f(np.array([x, Y[i, j]]))
ax.plot_surface(X, Y, Z)
plt.show()


# grad(f) = A^T (Ax - b)

np.random.seed(42)
x = (np.random.rand(2) - 0.5) * 20
# Step size, tolerance
epsilon, delta = 1e-1, 1e-5

iteration = 1
grad = A.T.dot(A.dot(x) - b)
while grad.dot(grad) > delta:
    x = x - epsilon * grad
    grad = A.T.dot(A.dot(x) - b)
    print('Iteration ' + str(iteration) + ': x = ' + str(x))
    iteration += 1

print('f(x) = ', f(x))
print('|grad| = ', grad.dot(grad))
