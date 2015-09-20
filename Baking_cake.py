


ingredients = {
"butter": ("butter", 118.3), 
"sugar": ("sugar", 236.6), 
"vanilla": ("vanilla", 4.929),
"eggs": ("eggs", 2), ## Whole eggs
"cocoa": ("cocoa", 118.3),
"flour":("flour", 118.3),
}
## Ingredients stored in a dictionary of tuples (with name and quantity in ml)

butter_soft = False  # boolean b/c butter was refrigerated
bowl = []  # the bowl is a list 

## Instructions for making the cake
def melt(this):
    print("Melting {0}.".format(this))

def bake(this, temp):
    print("Baking {0} at {1}.".format(this, temp))

def mix(this):
    print("Mixing {0}.".format(this)) 

def add_to_bowl(ingredient):
    print("Adding {0} to the bowl.".format(ingredient))
    return bowl.append(ingredient)       
    
## Algorithm to bake the cake

if butter_soft != True:
    melt(ingredients["butter"][0])
    butter_soft = True
    
add_to_bowl(ingredients["butter"][0])
add_to_bowl(ingredients["sugar"][0])

mixing_time = 0
mixture_creamy = False

# Mix until creamy
while mixture_creamy == False:
    mix(bowl)
    mixing_time += 1
    if mixing_time == 3: # after 3 minutes, the misture will be creamy
        mixture_creamy = True # the loop stops at creamy
        
add_to_bowl(ingredients["eggs"][0])
add_to_bowl(ingredients["vanilla"][0])

mixing_time = 0
well_blended = False

# Mix until well blended
while well_blended == False:
    mix(bowl)
    mixing_time += 1
    if mixing_time == 4:
        well_blended = True

## For baking move mixture of cake pan
cake_pan = bowl

cooking_temp = 350
cooking_time = 30

for minute in range(0, cooking_time):
    bake(cake_pan, cooking_temp)

print("The cake is done!")
    
    
        
        
        