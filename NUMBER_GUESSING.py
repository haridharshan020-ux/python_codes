import random

lower=1
upper=100
number=random.randint(lower,upper)
running=True
guess=0

print("welcome to the number guessing game!(1-100)")
while running:
    answer=(input(f"guess a number between {lower} and {upper}: "))
    if answer.isdigit():
        answer=int(answer)
        guess+=1
        if answer<lower or answer>upper:
                print("the guess is out of range,p;ease try again")
                answer = (input(f"guess a number between {lower} and {upper}: "))
        elif answer>number:
                 print("Too High,try again")
        elif answer<number:
                print("Too Low,try again")

        else:
                print(f"------CONGRATULATION YOUR GUESS IS CORRECT!!! IN {guess} ATTEMPTS------")
                break


    else:
        print("invalid input, please enter a number")
        answer=(input(f"guess a number between {lower} and {upper}: "))
