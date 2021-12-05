import random
print("Number guessing game")
number=random.randint(1,9)
chances=0
print("Guess a no. between 1 and 9:")
while chances<5:
    guess=int(input("Enter a guess:"))
    if guess==number:
        print("Congrats!You win!!")
        break;
    elif guess<number:
           print("Your guess is too low!Try a higher no.")
    else:
         print("Your guess is too high!Try a lower no.")  
    chances+=1
if not chances<5:
    print("You loose!The right answer is ") 
    print(number)