import random
import time

OPERATORS = ["+","-","/","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROB = 10

def generate_prob():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)

    return expr, answer

wrong = 0

start_time = time.time()

for i in range(TOTAL_PROB):
    expr, answer = generate_prob()
    while True:
        guess = int(input(" Problem # " + str(i+1) +" " + expr + "="))
        if guess == int(answer):
            break
        wrong+=1
        

end_time = time.time()


time_taken = round(end_time-start_time,2)


print("GREAT! YOU FINISHED IN ", time_taken," seconds")
print("You got ", 10-wrong," questions right!")