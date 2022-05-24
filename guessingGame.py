import random
number = random.randint(1, 10)
chanceCount = 0
while (chanceCount < 5):
    guess = int(input("enter the number between 1-10: "))
    if (guess > number):
        print("Your guess is too large")
    elif (guess == number):
        print("Congraulations you won!!!")
    else :
        print("Your number guess is too less")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("You are out of chances")