from neuron import Neuron

class Layer :

    def __init__(self, weights_list, biases_list):
        self.weights_list = weights_list    # ce doit être la matrice des poids de chaque neurone de la couche
        self.biases_list = biases_list      # ce doit être le vecteur de biais de la couche  

    def forward(self, inpt):
        # Construit la liste des sorties brutes de chaque neurone de la couche.
        outputs = []
        for i in range(len(self.weights_list)):
            value = Neuron(self.weights_list[i], self.biases_list[i]).forward(inpt)
            outputs.append(value) # On ajoute les valeurs brutes en sortie de neurone au fur et à mesure
        return outputs

    
