import numpy as np


class RBF:

	a = b = 0
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def sum(self):
		return self.a + self.b

X = np.zeros(5)
X[1] = 4
X[3] = 5
print(X)
d = np.random.choice(len(X), 2)
print(d)
print(X[d])