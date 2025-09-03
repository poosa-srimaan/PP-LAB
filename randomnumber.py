import random

n=random.randint(1,100)
print("GUESS THE NUMBER")

while(True):
	guess=int(input("guess the number: "))
	if guess==n:
		print("you won")
		break
	elif guess<n:
		print("your guess is low")
	elif guess>n:
		print("your guess is high")
