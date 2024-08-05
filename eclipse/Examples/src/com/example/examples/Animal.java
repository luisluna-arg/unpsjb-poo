package com.example.examples;

public class Animal implements Playable {
    public void makeSound() {
        System.out.println("Animal makes sound");
    }
    
    @Override
    public void play() {
        System.out.println("Animal is making a sound");
    }
}
