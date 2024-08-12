package com.example.main;

import com.example.animal.Dog;
import com.example.zoo.Zoo;

public class App {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.move();

        // Using the static class
        Zoo.Cage cage = new Zoo.Cage();
        cage.displayAnimal(dog);
    }

}
