print("***Addition Game***")
keep_going = input("***Press <enter> to continue***")
print("Addition game is a maths quiz where the questions get more difficult the more you keep playing")
keep_going = input("***Press <enter> to start quiz***")
print("*************** Game in Progress ***************")
keep_going = input("***Press <enter to continue***")
while keep_going == "":
    import random
    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("5+5=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)
    how_much = intcheck("Select the number of questions? ", 10,10)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("10+10=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 20, 20)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("20+20=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 40, 40)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("40+40=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 80, 80)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("80+80=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 160, 160)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("160+160=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 320, 320)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("320+320=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 640, 640)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("640+640=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 1280, 1280)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("1280+1280=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 2560, 2560)
    print("correct")
    keep_going = input("***Press <enter> to continue***")
    import random


    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Whoops! Your answer is incorrect try again ".format(low, high)

            try:
                response = int(input("2560+2560=".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


    how_much = intcheck("Select the number of questions? ", 5120, 5120)
    print("correct")
    print()
    print("***congratulations!***")
    keep_going = "end"
else:
    keep_going = input("Press <enter> to to quit")