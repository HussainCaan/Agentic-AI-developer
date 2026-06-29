def cook_And_mix():
    print("Mixing the ingredients:")
    print("Pouring the mixture into a hot pan.")
    print("Cooking the first side")
    print("Flipping the omelette to cook the other side.")

def make_fancy_omelette(*ingredients):
    
    cook_And_mix()
    return print(f"Enjoy your {ingredients} omelette!\n")
    

# def cookOmmelette(ingredients):
    
#     cook_And_mix()
#     return print(f"Enjoy your delicious {ingredients} omelette!\n")

def cookPencake():
    cook_And_mix()
    return print("Enjoy your delicious pancake!\n")

    

mybreakfast = make_fancy_omelette(['bacon', 'cheese', 'mushrooms'])
herbreakfast = make_fancy_omelette(['spam', 'onions', 'peppers'])