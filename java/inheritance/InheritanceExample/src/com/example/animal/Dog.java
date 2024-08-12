package com.example.animal;

public class Dog extends Mammal {
    
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }

    @Override
    public void move() {
        System.out.println("The dog runs.");
    }
}
