from neuron import Neuron

class Layer :

    def __init__(self, weights_list, biases_list):
        self.weights_list = weights_list    # ce doit être la matrice des poids de chaque neurone de la couche
        self.biases_list = biases_list      # ce doit être le vecteur de biais de la couche  

    def forward(self):
        Neuron.forward
    # il faut faire en sorte de créer une liste à partir des résultats de Neuron.forward pour chaque neurone de la couche
    