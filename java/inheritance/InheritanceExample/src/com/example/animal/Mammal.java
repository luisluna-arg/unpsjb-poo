package com.example.animal;

public abstract class Mammal implements IAnimal {
    
    @Override
    public String getType() {
        return "Mammal";
    }

    // Abstract method
    public abstract void move();
}