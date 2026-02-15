from neuron import Neuron

class Layer :

    def __init__(self, weights_list, biases_list):
        self.neurons = []
        for i in range(len(weights_list)):
            n = Neuron(weights=weights_list[i], bias=biases_list[i])
            self.neurons.append(n)
        
    def forward(self, inputs):
        # Construit la liste des sorties brutes de chaque neurone de la couche.
        return [n.forward(inputs) for n in self.neurons]

    
