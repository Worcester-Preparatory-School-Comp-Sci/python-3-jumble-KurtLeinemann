#Kurt Leinemann September 30 2019
#This game scrables a list of words and lets a user guess random words for points
from random import *
def wordJumble():
	score = 0;
	title()
	for i in range(0,5):			#loops once for each word								
		listWords=["cheeseburger","sandwich","turkey","pizza","sushi","applesauce","corn","potato","cake","cookie","soup","biscuit","cereal","banana","pudding","cracker","chips","popcorn","bread","cheesecake","pie","fruit","watermelon","taco","avocado","beans","pineapple","sausage","bacon"]
		wordCount = (len(listWords)-1)
		randNum=randint(0,wordCount)
		randWord=listWords[randNum]
		scramble(randWord)
		guess=str(input("What word is this?"))
		if guess==randWord:
			print("You got it")
			score+=10
		else:
			print("Nope, the word was",randWord)
	print("Your score is:",score)
	print("Thank you for playing!")
		
#This function scrambles the selected random word
def scramble(randWord):
	jumbledWord=""
	wordLength=len(randWord)
	while wordLength>1:     #while there is word, remove a letter at random and add it to a new word (jumbledWord)
		wordLength=len(randWord)
		randomLetterPos=randint(0,wordLength)
		if randomLetterPos == wordLength:
			randomLetterPos =0
		jumbledWord=jumbledWord+randWord[randomLetterPos]	
		randWord=randWord[:randomLetterPos]+randWord[(randomLetterPos+1):]	
	print(jumbledWord)
	
def title(): #displayed before game officially starts
	title = "Food Scramble Game!"
	print(title)
	print("")
	print("by Kurt Leinemann")
	print("Enter to continue")
	cnt=input()
wordJumble()	



