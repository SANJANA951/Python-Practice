from random import randint

c =  randint(1,100)


i = 0
b = 1
guesses = 1
while True:
    y = int(input("Guess the number: "))


    if(c>y):
       print("Bigger number please")
       guesses += 1
    elif(c<y):
        print("Smaller number please")
        guesses += 1
    elif(y<1 or y>100):
        print("You have to guess the number between 1 to 10")
        guesses += 1
    else:
        print(f"You have guessed the number {c} correctly in {guesses} attempts  ")
        break 
    