import random
number = random.randint(1,9)

print("Number Guesiing Game")
print("Guess a number (between 1 to 9)")

chances = 0

while chances < 5 :

    guess = int(input("Enter a guess :-"))
    chances = chances + 1

    if (guess < number):
        
        print("Your guess was too low : Guess a number higher than", guess)

    elif (guess > number) :
        
        print ("Your guess was too high : Guess a number lower than", guess)
    elif (guess == number) :
        print("Congratulation YOU WON ! ! !")
        break
    else:
        print("Wrong Code")

if not chances < 5:
     print("YOU LOSE! The number is ", number)