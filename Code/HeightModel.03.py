##### Defining Parameters ######
# Note that we define the parameters *outside* of the function definition
# and at the top of the code. This makes it easier to change

a1 = 1.3 # A number between 1 and 2. A higher value means the
#          son's height will more closely match the fathers
a2 = 1.3 # A number between 1 and 2. A higher value means the
#          daughters's height will more closely match the mothers

##### Defining Variables ######
# h1 is the father's height, h2 is the mother's height
# male is a Boolean variable (either True or False)

# To execute the childs_height function you would type something like:
#  childs_height(1.8, 1.65, False) for a daughter who's father is 1.8m tall
# and who's mother is 1.65m tall.


###### Defining the model #########

def sons_height(h1, h2): 
    h = ( a1*h1 + (2-a1)*h2 ) / 2
    return(h)

def daughters_height(h1, h2): 
    h = ( (2-a2)*h1 + a2*h2 ) / 2
    return(h)

def childs_height(h1, h2, male): 
    if male:
        h = sons_height(h1, h2)
    else:
        h = daughters_height(h1, h2)
    return(h)

####################################

########## Testing the model ###############
# The following list is a test data set of family heights
# Each element of the list is another list in the following format:
# [fathers height, mothers height, sons height, daughters height]

hdata = [[1.62,1.69,1.71,1.66], [1.55,1.74,1.7,1.6], [1.7,1.67,1.73,1.66], [1.85,1.73,1.8,1.72], [1.78, 1.54, 1.76, 1.62]]
print("")
print("__________________________________________________")
print("Testing model with parameters: a1 =",a1,", a2 =",a2)
print("__________________________________________________")
print("")

for family_data in hdata:
    fh = family_data[0]
    mh = family_data[1]
    sh = family_data[2]
    dh = family_data[3]
    # Testing the model, printing the results
    print("Testing on family data:", family_data)
    print("      Predicted son height of", childs_height(fh, mh, True), "compared to actual height of", sh)
    print("      Predicted daughter height of", childs_height(fh, mh, False), "compared to actual height of", dh)
    print("")
    


