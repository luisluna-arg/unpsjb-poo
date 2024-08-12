class SwitchExample:
    def print_day(self, day_number):
        print("")
        print("SwitchExample")
        if day_number == 1:
            day = "Monday"
        elif day_number == 2:
            day = "Tuesday"
        elif day_number == 3:
            day = "Wednesday"
        elif day_number == 4:
            day = "Thursday"
        elif day_number == 5:
            day = "Friday"
        elif day_number == 6:
            day = "Saturday"
        elif day_number == 7:
            day = "Sunday"
        else:
            day = "Invalid day number"
        
        print("The day is", day)
