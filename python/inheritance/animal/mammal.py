from abc import ABC, abstractmethod

class Mammal(ABC):
    def get_type(self) -> str:
        return "Mammal"
    
    @abstractmethod
    def move(self) -> None:
        ...
