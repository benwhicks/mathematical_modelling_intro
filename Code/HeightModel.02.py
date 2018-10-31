##### Defining Parameters ######
# Note that we define the parameters *outside* of the function definition
# and at the top of the code. This makes it 
a1 = 2.5
a2 = 0.9

##### Defining Variables ######
# h1 is the father's height, h2 is the mother's height

def sons_height(h1, h2): 
    h = ( a1*h1 + (2-a1)*h2 ) / 2
    return(h)

def daughters_height(h1, h2): 
    h = ( (2-a2)*h1 + a2*h2 ) / 2
    return(h)


