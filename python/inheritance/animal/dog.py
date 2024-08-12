from animal.mammal import Mammal

class Dog(Mammal):
    def make_sound(self) -> None:
        print("Bark")
    
    def move(self) -> None:
        print("The dog runs.")
