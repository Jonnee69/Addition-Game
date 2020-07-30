# Addition Game Decomposition Step 1
# Get initial amount and check that it's valid

# Integer checking function
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter a question between {} " \
                "and {}".format(low, high)

        try:
            response = int(input("Select how many questions you want with numbers between {} "
                                 "and {}: ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine goes here here

how_much = intcheck("Select the number of questions? ", 1, 10)
