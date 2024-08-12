from typing import Protocol

class Animal(Protocol):
    def make_sound(self) -> None:
        ...
    
    def get_type(self) -> str:
        ...
