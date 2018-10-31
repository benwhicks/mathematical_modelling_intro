# Starting model
# To use this model first Run the module (F5 or select Run -> Run Module)
# Once you have run the module you can then type in:
#    child_height(1.4, 1.8)
# and the model should output a result


# h1 is the fathers height, h2 is the mothers height

def child_height(h1, h2): 
    h = (h1 + h2)/2
    return(h)

