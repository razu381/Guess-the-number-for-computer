import random
import time

random_num = random.randint(1,100)
comp_guess = 0
low = 1
high = 100
step_required = 0
comp_guess_stn = ["I think it's ","How about ", "it's gotta be ", "uff, it's must be ","oh, it's pretty hard to guess huh! how about "]
print("You: Guess a number between 1 - 100")



while comp_guess != random_num:
    comp_guess = random.randint(low,high)
    comp_random_guess_stn = random.randint(0,4)
    if comp_guess > random_num:
        print(f"Computer: {comp_guess_stn[comp_random_guess_stn]}{comp_guess}")
        time.sleep(1)
        print(f"You: No,think of a number smaller than {comp_guess}")
        step_required += 1 
        high = comp_guess+1
        print("Thinking.........................")
        time.sleep(2)
    elif comp_guess < random_num:
        print(f"Computer: {comp_guess_stn[comp_random_guess_stn]}{comp_guess}")
        time.sleep(1)
        print(f"You: No,think of a number bigger than {comp_guess}")
        step_required += 1
        low = comp_guess+1
        print("Thinking.........................")
        time.sleep(2)
    else:
        print(f"Computer: {comp_guess_stn[comp_random_guess_stn]}{comp_guess}")
        print(f"You: You are correct, the number is indeed {comp_guess}")
        step_required += 1
    
print(f"It took you {step_required} guesses")
    