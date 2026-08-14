from random import randint

n = randint(1,100)
a = -1
guesses = 1

while(a != n):

    a = int(input("Guess the number please:"))

    if(a > n):
        print("chota number please!")
        guesses += 1
    elif(a < n):
        print("Bada number please!")
        guesses += 1
    
    else:
        print(f"You have guessed the correct number {n} in  {guesses} attempts ")

