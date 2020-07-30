# Allow manual question input for a testing purposes
questions = input("Select the number of questions? ")

import random

questions = ["5+5", "10+10", "20+20", "40+40", "80+80", "160+160", "320+320", "640+640", "1280+1280", "2560+2560"]

for item in range(1):

    chosen = random.choice(questions)
    print(chosen)
