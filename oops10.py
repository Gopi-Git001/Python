def myfunc():

    while True:
        try:
            number = int(input("Enter a number: "))
            print(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        else:
            break   
        finally:
            print("The try except is finished")

myfunc()