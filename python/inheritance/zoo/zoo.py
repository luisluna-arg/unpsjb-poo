from animal.animal import Animal

class Zoo:
    @staticmethod
    def display_animal(animal: Animal) -> None:
        print(f"Animal Type: {animal.get_type()}")
        animal.make_sound()
