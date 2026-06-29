class Jeans:
    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length 
        self.color = color
        self.wearing = False
        
    def put_on(self):
        print(f"Putting on jeans with waist {self.waist}, length {self.length}, and color {self.color}.")
        self.wearing = True
        
    def take_off(self):
        print(f"Taking off jeans with waist {self.waist}, length {self.length}, and color {self.color}.")
        self.wearing = False
    

    