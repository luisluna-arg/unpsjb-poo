package com.example.zoo;

import com.example.animal.IAnimal;

public class Zoo {

    public static class Cage {
        public void displayAnimal(IAnimal animal) {
            System.out.println("Animal Type: " + animal.getType());
            animal.makeSound();
        }
    }
}
