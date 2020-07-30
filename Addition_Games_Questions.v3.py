def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter a question between {} " \
                "and {}".format(low, high)

        try:
            response = int(input("Select how many questions you want with numbers between {} "
                                 "and {}? ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)
# Allow manual token input for a testing purposes
how_much = intcheck("Select the number of questions? ", 1, 10)

import random
questions = ["5+5", "10+10", "20+20", "40+40", "80+80", "160+160", "320+320", "640+640", "1280+1280", "2560+2560"]

for item in range(1):

    chosen = random.choice(questions)
    print(chosen)
keep_going = "end"
keep_going = input("Press <enter> to play again or any to quit")
