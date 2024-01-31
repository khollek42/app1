


try:
    width = float(input("Enter rectangle witdh: "))
    length = float(input("Enter rectangle length: "))

    #checks if it is a square prints message and exits

    if width == length:
        exit("That is a square.")


    area = width * length
    print(area)
#catches exception and tells user the input needs to be a number.
except ValueError:
    print("please enter a number.")