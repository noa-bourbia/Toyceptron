class Neuron: 
	def __init__(self, weights, bias):
		self.weights = weights
		self.bias = bias

	def forward (self, inputs):
		total = 0
		for  i in range(len(inputs)):
			total += inputs[i] * self.weights[i]
			
		return total + self.bias
