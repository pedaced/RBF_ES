import numpy as np
import random


class RBF:

	def __init__(self, X):
		self.W = None
		self.y = random.random() * 100
		self.ERR = 10000.
		self.hidden_neurons = 10
		self.V = np.random.rand(hidden_neurons) * 100

	def set_parameters(self, V, y):
		self.V = V
		self.y = y

	def _kernel_function(self, X, Y):
		return np.exp(-y * np.dot(np.transpose(y), y))


	def fit(self, X, Y):
		G = self._calculate_G(X)
		self.W = np.dot(np.lingalg.inv(np.dot(np.transpose(G), G)), np.transpose(G)) * self.y

	def _calculate_G(self, X):
        G = np.zeros((len(X), self.hidden_neurons))
        for data_point_arg, data_point in enumerate(X):
            for V_arg, v in enumerate(self.V):
                G[data_point_arg, V_arg] = self._kernel_function(
                        v, data_point)
        return G

	def _calculate_error(self, Y):
		return np.dot(np.transpose(Y - y), Y - y) / 2.0

	def predict(self, X):
		G = self._calculate_G(X)
		new_Y = np.dot(G, self.W)
		self._calculate_error(new_Y)
		return new_Y

	def get_error_rate(self):
		return self.ERR


print(random.random())

