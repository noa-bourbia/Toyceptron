# imports :
from math import exp
    # import de la fonction exp du module math qui est déjà implémenté de base
from network import Network
from neuron import Neuron
# from activation import act_relu, act_threshold, act_identity
    # import des classes que nous avons définies au sein des modules network et neuron (qui correspondent aux fichiers respectifs)


def act_sigmoid(x):
    return 1 / (1 + exp(-x))
    # definition de la fonction d'activation sigmoide

# --- Input ---
x = [1.0, 2.0, 4.0]
print("Input:", x)
    # Ce que Felix appelle imput est en réalité le vecteur correspondant aux activations de la couche 0



# --- Test neurone individuel ---
print("\n--- Test Neuron ---")
# les neurones ont 3 poids pour correspondre à la taille de notre input
n1 = Neuron(weights=[0.2, -0.1, 0.4], bias=0.0)     # Création d'un objet neurone n1
n2 = Neuron(weights=[-0.4, 0.3, 0.1], bias=0.1)

out_n1 = n1.forward(x)      # Retourne la valeur que l'on donne à la fonction d'activation du neurone
out_n2 = n2.forward(x)
print("Neurone h1 (brut):", out_n1)  # 1.6
print("Neurone h2 (brut):", out_n2)  # 0.7
print("Neurone h1 (activé):", act_sigmoid(out_n1))  # 0.8320183851339245    valeur d'activation en sortie de fonction
print("Neurone h2 (activé):", act_sigmoid(out_n2))  # 0.6681877721681662



# --- Test couche cachée ---
print("\n--- Test Layer ---")
# Mêmes valeurs, mais on ajoute les deux neurones en une seule fois dans la couche
# On devrait avoir des résultats identiques

from layer import Layer

layer = Layer(                  # Création d'un objet layer
    weights_list=[              # Matrice des poids
        [0.2, -0.1, 0.4],
        [-0.4, 0.3, 0.1],
    ],
    biases_list=[0.0, 0.1],     # vecteur des biais 
)

raw = layer.forward(x)      # Appel de la fonction forward de la classe layer, cette fonction prend les valeurs "brutes" des neurones et les transforme en liste
                            # raw est donc une liste qui renvoie les valeurs brutes des neurones
activated = [act_sigmoid(o) for o in raw]   # activated parcourt raw (pour raw data) et la transforme en la liste des valeurs d'activation des neurones de la couche 1
print("Couche (valeurs brutes):", raw)  # [1.6, 0.7]
print("Couche (valeurs activées):", activated)  # [0.8320183851339245, 0.6681877721681662]



# --- Test du réseau entier ---
print("\n--- Test Network ---")
net = Network(input_size=3, activation=act_sigmoid)     # Création d'un objet net qui a en paramètres input_size et activation
                                                        # activation semble être la fonction d'activation choisie
                                                        # input size est la taille du vecteur imput


# 1. On commence par une couche "cachée"
    # Ce que Felix ici décrit comme une couche cachée est en réalité toutes les couches intermédiaires autre que la couche d'inputs et la couche de sortie

net.add(                    # ok donc il existe une fonction add à net
    weights=[               # matrice des poids (la couche 0 a 3 "neurones" et la couche 1 en a 2)
        [0.2, -0.1, 0.4],
        [-0.4, 0.3, 0.1],
    ],
    biases=[0.0, 0.1],      # vecteur des biais    
)

# 2. La deuxième couche est cachée aussi
net.add(
    weights=[
        [0.5, -0.2],  # la taille correspond au nombre de neurones couche 1 (la couche 1 a 2 neurones et la couche 2 en a 3)
        [-0.3, 0.4],
        [0.1, 0.2],
    ],
    biases=[0.0, 0.1, -0.1],
)

# 3. Couche de sortie
net.add(
    weights=[
        [0.3, -0.1, 0.2],  # taille = nombre de neurones couche 2
        [-0.5, 0.4, 0.1],
    ],
    biases=[-0.1, 0.0],
)

# Feedforward complet (via Network)
y = net.feedforward(x)      # il y a donc une fonction feedforward à la classe net
print("\nSorties activées :", y)  # [0.5309442148001715, 0.494901997674804]


# Feedforward couche par couche (mêmes résultats en théorie)
inputs = x
for i, layer in enumerate(net.layers):
    raw = layer.forward(inputs)
    activated = [act_sigmoid(o) for o in raw]
    print(f"\nCouche {i + 1} (valeurs brutes):", raw)
    print(f"Couche {i + 1} (valeurs activées):", activated)
    inputs = activated
