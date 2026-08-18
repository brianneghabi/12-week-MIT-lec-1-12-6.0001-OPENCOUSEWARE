import random
import time


print(" hello welcome to the number guessing game")
time.sleep(2)
print("please select the level of dificullty")

user_input = input("  easy----medium----Hard---imposible")




if user_input == "easy" or user_input == "Easy":
    print("you have 15 guesses to guess the number between 1 and 100")
    random_number = random.randint(1, 100)
    for i in range(15):
        user_guess = int(input("please enter your guess: "))
        if user_guess == random_number:
           print(f"congratulations the number was {random_number}, you guessed the number in {i + 1} tries. nice you tryied and you won")
           break
           
        elif user_guess < random_number:
            print("your guess is too low")
        elif user_guess > random_number:
            print("your guess is too high")
        if i == 15:
            print(f"you have used all your guesses the number was {random_number} damn better luck next time")



elif user_input == "medium" or user_input == "Medium":
    print("you have 10 guesses to guess the number between 1 and 100")
    random_number = random.randint(1, 100)
    for i in range(10):
        user_guess = int(input("please enter your guess: "))
        if user_guess == random_number:
            print(f"congratulations the number was {random_number}, you guessed the number in {i + 1} tries.you might think youre avarage but your not your good at this game")
            break

        elif user_guess < random_number:
            print("your guess is too low")
        elif user_guess > random_number:
            print("your guess is too high")
        if i == 4:
            print(f"you have used all your guesses the number was {random_number} nice job you tried but you lost but that is the key to winning you have to keep trying and never give up")

elif user_input == "hard" or user_input == "hard":
    print("you have 5 guesses to guess the number between 1 and 100")
    random_number = random.randint(1, 100)
    for i in range(5):
        user_guess = int(input("please enter your guess: "))
        if user_guess == random_number:
            print(f"congratulations the number was {random_number}, you guessed the number in {i + 1} tries.wow you are super good at this game you might be a genius")
            break

        elif user_guess < random_number:
            print("your guess is too low")
        elif user_guess > random_number:
            print("your guess is too high")
        if i == 5:
            print(f"you have used all your guesses the number was {random_number} nice job even though you think you are bad just know you whrere on the the 2nd to last hardest dificulltiy")




elif user_input == "imposible" or user_input == "imposible":
    print("you have 1 guess to guess the number between 1 and 100")
    random_number = random.randint(1, 100)
    for i in range(1):
        user_guess = int(input("please enter your guess: "))
        if user_guess == random_number:
            print(f"congratulations the number was {random_number}, you guessed the number in {i + 1} tries.YOU ARE A PRODIGY!!!!")
            break
        elif user_guess < random_number:
            print("your guess is too low,Im sorry but you lost")
        elif user_guess > random_number:
            print("your guess is too high,Im sorry but you lost")
        if i == 1:
            print(f"you have used all your guesses the number was {random_number} its fine imposible is preaty much imposible")


