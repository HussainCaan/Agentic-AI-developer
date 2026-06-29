class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4
        
    def drive(self):
        if self.gas > 0:
            print("The vehicle is driving.")
            self.gas -= 1
        else:
            print("The vehicle is out of gas and cannot drive.")


class Car(Vehicle):
    def radio(self):
        print("The car's radio is playing music.")
    
    def window(self):
        print("The car's window is rolled down.")
    
class MoterCycle(Vehicle):
    def helmet(self):
        print("The motorcycle rider is wearing a helmet.")
    
    def kickstand(self):
        print("The motorcycle's kickstand is down.")
        

class ECar(Car):
    def drive(self):
        print("The electric car is in autopilot mode. And Going Non STOP!!!!")