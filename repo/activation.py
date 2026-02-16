def act_relu(x):
    if x < 0 :
        return 0
    else :
        return x

def act_threshold(x):
    if x > 0 :
        return 1
    else :
        return 0
    
def act_identity(x):
    return x
