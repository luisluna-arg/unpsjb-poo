class DoWhileExample:
    def repeat_message(self):
        print("")
        print("DoWhileExample")
        count = 1
        while True:
            print("This is message number", count)
            count += 1
            if count > 3:
                break
