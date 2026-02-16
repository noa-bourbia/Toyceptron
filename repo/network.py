from layer import Layer

class Network:
    def __init__(self, input_size, activation):
        self.layers = []
        self.activation = activation # La fonction (ex: sigmoïde) 

    def add(self, weights, biases):
        # Ajoute une nouvelle couche au réseau 
        self.layers.append(Layer(weights, biases))

    def feedforward(self, inputs):
        current_input = inputs
        for layer in self.layers:
            # 1. Calcul brut par la couche
            raw_outputs = layer.forward(current_input)
            # 2. Application de la fonction d'activation sur chaque sortie 
            current_input = [self.activation(val) for val in raw_outputs]
        return current_input