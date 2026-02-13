import random

class Neuron:
    def __init__(self, weights, bias, size=0):
        if weights == None:
            self.weights = []
            for i in range (size) :
                self.weights.append(random.uniform(-1,1))   
        else:    
            self.weights = weights

        if bias == []:
            self.bias = random.uniform(-1,1)    
        else :    
            self.bias = bias



    def forward(self, inpt):
        # Calcule z = w·x + b (produit scalaire + biais).
        total = 0.0
        for i in range (len(inpt)):
            total += float(self.weights[i]) * float(inpt[i])
        total += self.bias
        return total