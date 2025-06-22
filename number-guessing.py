import random

chances = 8

number  = random.randint(1,100) # random no b/w 1 and 100

while (chances>0):
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Correct ANSWER!!!")
        break
    elif guess > number:
        print("Guess too HIGH")
    else: 
        print("Guess too LOW")

    chances -= 1
    print("Chances left: ",chances)


if chances == 0:
    print(f"Out of chances. The numbewwr was {number}")



    



