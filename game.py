import random

# welcome statement
print("===========================================")
print("Welcome to the game of Rock Paper Scissors.")
print("Type Rock/Paper/Scissors, and press Enter. ")
print("===========================================")

player = input("You: ").lower()
bot = random.randint(1, 3)

if (bot==1):
    bot = "rock"
elif (bot==2):
    bot = "paper"
elif (bot==3):
    bot = "scissors"

print("Bot:",bot)

if(player==bot):
    print("It is a tie!")
elif((player=="rock" and bot=="scissors") or (player=="paper" and bot=="rock") or (player=="scissors" and bot=="paper")):
    print("You Win!")
else:
    print("You Lose!")