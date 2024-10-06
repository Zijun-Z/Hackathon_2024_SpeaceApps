with open("1000WordDatabase.txt","r") as f :
	for e in f:
		e = e.replace("\n","")
		database.append(e)

from random import randint
from time import sleep
import time


def typing(database):
	print("During you work, you boss asks you to make a transcript of his speech.Your task is to type each word as fast as possible. Your boss makes it clear that the size of your paycheck will depend on your performance")
	print("You will be given a word. Type it as fast as you can without spelling mistakes. Do this 10 times to get an average time per word.")
	while True:
		t = time.time()
		for i in range(10):
				word = random.choice(database)
				end = False
				print(f"Your word is '{word}'\n")
				 
				while end == False:
					answer = input(f'Type the word! ({10-i} words left)\n\n')
					if answer == word:
						end = True
						print(f'It took you {round(time.time()-t)} sec.')
					else:
						print(f"You got it wrong! Try again. The word is {word}")
		back = input(f"You wrote 10 words in {round((time.time()-t)*100)/100} seconds. That's {round(10/(time.time()-t)*100)/100} words per second\n")
		print(f"Your income is {round((1/round(time.time()-t))*35000)}")
		income = round((1/round(time.time()-t))*35000)
		
def memory():
	memoryWord = ""
	print("During your work, your boss wants you to remember as much of his password as you can (no one knows why it is so long). It is clear that your performance will impact your income")
	level_memory = 1
	while True:
		memoryWord += str((randint(0,9)))
		print("You have 2 seconds to remember this number ->",memoryWord)
		sleep(2)
		answer = input("What was the number?")
		if answer == memoryWord :
			level_memory += 1
			input("Good job! Your level has increased.")
		else:
			print(f"Your income is {(143/7)*(level_memory**2)+999}")
			income = (143/7)*(level_memory**2)+999
			
def reaction():
	total_time = 0
	print("Many people interview you during your protest. Depending on how fast you can come up with a response, your protest could go better or worse.")
	while True:
		print("At the end of the countdown, press ENTER as fast as possible to see how fast you can respond. This will happen 3 times to get an average response time")
		for i in range(3):
			print("3")
			sleep(0.1)
			print("2")
			sleep(0.1)
			print("1")
			sleep(randint(1,6)/randint(1,4))
			t = time.time()
			input(f"Go!")
			total_time += (time.time()-t)
	score = round((total_time)*1000)/1000

def speed():
	duration = 3
	points = 0
	print("During the protest, you try to start a chant that will be heard by as many as possible. Your score in this minigame will represent how loud your chant was.")
	input(f"You will be given a number. During the next {duration} seconds you will have to submit (enter) this number as many times as you can.")
	t = time.time()
	numberGiven = str(randint(0,9))
	while (time.time()-t < duration):
		if input(f"Enter {numberGiven} as many times as you can! You only have {round(duration-(time.time()-t))} seconds.") == numberGiven:
			points+=1
	menu = input(f"You got {points} numbers in {duration} seconds!. That's an average of {round(points/duration*100)/100} points per second.")
	score = round(points/duration*100)/100
