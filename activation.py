def act_identity(x):
    return x # Renvoie la valeur telle quelle 

def act_threshold(x):
    return 1 if x > 0 else 0 # Renvoie 1 ou 0 

def act_relu(x):
    return max(0, x) # Renvoie x si positif, sinon 0 
