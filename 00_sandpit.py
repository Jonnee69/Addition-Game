import random

to_double = random.randint(1, 1000)

question = "{} + {}".format(to_double, to_double)
answer = eval(question)

print("Question: {} = ".format(question))
print("Answer: {}".format(answer))