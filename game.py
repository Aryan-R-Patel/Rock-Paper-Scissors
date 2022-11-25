import random

# welcome statement
print("===========================================")
print("Welcome to the game of Rock Paper Scissors.")
print("To start playing, simply enter Rock or Paper")
print("or Scissors and then press Enter.          ")
print("===========================================")

player = input("You: ").capitalize()
bot = random.randint(1, 3)

if (bot==1):
    bot = "Rock"
elif (bot==2):
    bot = "Paper"
elif (bot==3):
    bot = "Scissors"

print("Bot:",bot)

if(player==bot):
    print("It is a tie!")
elif((player=="Rock" and bot=="Scissors") or (player=="Paper" and bot=="Rock") or (player=="Scissors" and bot=="Paper")):
    print("You Win!")
else:
    print("You Lose!")