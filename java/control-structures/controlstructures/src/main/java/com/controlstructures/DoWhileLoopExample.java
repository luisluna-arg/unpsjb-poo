package com.controlstructures;

public class DoWhileLoopExample {
    public static void repeatMessage() {
        System.out.println("");
        System.out.println("DoWhileLoopExample");
        int count = 1;
        do {
            System.out.println("This is message number " + count);
            count++;
        } while (count <= 3);
    }
}
