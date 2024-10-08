package com.example.main;
import com.example.examples.*;

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        Animal myCat = new Cat();
        
        myDog.makeSound(); // Outputs: Bark
        myDog.play(); // Outputs: Bark
        
        System.out.println();
        myCat.makeSound(); // Outputs: Meow
        myCat.play(); // Outputs: Meow

        System.out.println();
        
        Student student = new Student("Alice", 22, "S12345");
        student.displayInfo(); // Outputs: Name: Alice, Age: 22, Student ID: S12345
    }
}
