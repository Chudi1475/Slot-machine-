# slot machine game
#auto commit set up

#this way
import random
if __name__ == "__main__":
    print("Welcome to the slot machine game!")
    print("You can bet between 1 and 100 credits.")
    print("Good luck!")
    while True:
        bet = int(input("How many credits do you want to bet? "))
        if bet < 1 or bet > 100:

