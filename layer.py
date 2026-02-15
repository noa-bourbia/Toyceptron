from neuron import Neuron

class Layer:
from neuron import Neuron

class Layer:
    def __init__(self, weights_list, biases_list):
        # Une couche est une collection de neurones 
        # On crée chaque neurone à partir des listes reçues 
        self.neurons = []
        for i in range(len(weights_list)):
            n = Neuron(weights=weights_list[i], bias=biases_list[i])
            self.neurons.append(n)

    def forward(self, inputs):
        # On applique l'entrée à tous les neurones de la couche 
        # Tous les neurones reçoivent le même vecteur d'entrée 
        
return [n.forward(inputs) for n in self.neurons]    def __init__(self, weights_list, biases_list):
        self.neurons = []
        for i in range(len(weights_list)):
            n = Neuron(weights=weights_list[i], bias=biases_list[i])
            self.neurons.append(n)

    def forward(self, inputs):
        return [n.forward(inputs) for n in self.neurons]
