# Q10 Number Guessing Game.
# Letʼs create a “Number Guessing Game”. Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:
# •"Too high" if the guess is above the number
# •"Too low" if the guess is below
# •"Correct!" if the guess matches

n = int(input("Enter the secret number:"))
i=0
while(i!=n):
   i=int(input("Guess the number: "))
   if(i>n):
        print("Too high")
   elif(i==n):
        print("Correct!")
   else:
       print("Too low")
