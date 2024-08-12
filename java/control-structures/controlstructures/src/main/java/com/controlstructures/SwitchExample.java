package com.controlstructures;

public class SwitchExample {
    public static void printDay(int dayNumber) {
        System.out.println("");
        System.out.println("SwitchExample");
        String day;
        System.out.println("    Regular switch");
        switch (dayNumber) {
            case 1:
                day = "Monday";
                break;
            case 2:
                day = "Tuesday";
                break;
            case 3:
                day = "Wednesday";
                break;
            case 4:
                day = "Thursday";
                break;
            case 5:
                day = "Friday";
                break;
            case 6:
                day = "Saturday";
                break;
            case 7:
                day = "Sunday";
                break;
            default:
                day = "Invalid day number";
                break;
        };
        System.out.println("    The day is " + day);
        System.out.println("");
        System.out.println("    Switch expression");
        day = switch (dayNumber) {
            case 1 -> "Monday";
            case 2 -> "Tuesday";
            case 3 -> "Wednesday";
            case 4 -> "Thursday";
            case 5 -> "Friday";
            case 6 -> "Saturday";
            case 7 -> "Sunday";
            default -> "Invalid day number";
        };
        System.out.println("    The day is " + day);
    }
}
