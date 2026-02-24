import random
print("Welcome to Name Gussing Game!" \
"\n You Have to guess the number within 7 chances")
low =int(input("Enter the lower limit: "))
high=int(input("Enter the upper limit: "))
print(f"Guess the number between {low} and {high}")
num =random.randint(low, high)
chance = 7
while chance > 0:
    guess= int(input("Enter the number: "))
    if guess==num:
        print("Congratulations ! you won")
        break
    elif guess>num:
        print("Too high")
    else:
        print("Too low")
    chance -= 1
if chance == 0:
    print(f"Sorry! you lost. The number was {num}")
