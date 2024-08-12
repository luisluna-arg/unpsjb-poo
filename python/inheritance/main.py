from animal.dog import Dog
from zoo.zoo import Zoo


def main():
    dog = Dog()
    dog.move()
    
    # Using the static method
    Zoo.display_animal(dog)

if __name__ == "__main__":
    main()
