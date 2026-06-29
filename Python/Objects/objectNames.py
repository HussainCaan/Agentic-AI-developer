class Shirt:
    def __init__(self):
        self.clean = True
    
    def dirty(self):
        self.clean = False
        print("The shirt is now dirty.")
        
    def wash(self):
        self.clean = True
        print("The shirt is now clean.")