import random
#prints out hangman figure
def printMan(n):
	if n == 0:
		print("   _ _     ")
		print("  |        ")
		print("  |        ")
		print("__|________")
	if n == 1:
		print("   _ _     ")
		print("  |   O    ")
		print("  |        ")
		print("  |        ")		
		print("__|________")
	if n == 2:
		print("   _ _     ")
		print("  |   O    ")
		print("  |   |    ")
		print("  |        ")
		print("__|________")
	if n == 3:
		print("   _ _     ")
		print("  |   O    ")
		print("  |  /|    ")
		print("  |        ")
		print("__|________")		
	if n == 4:
		print("   _ _     ")
		print("  |   O    ")
		print("  |  /|\   ")
		print("  |        ")
		print("__|________")
	if n == 5:
		print("   _ _     ")
		print("  |   O    ")
		print("  |  /|\   ")
		print("  |  /     ")
		print("__|________")
	if n == 6:
		print("   _ _     ")
		print("  |   O    ")
		print("  |  /|\   ")
		print("  |  / \   ")
		print("__|________")
	if n == 7:
		print("   _ _     ")
		print("  |   O    ")
		print("  | _/|\   ")
		print("  |  / \   ")
		print("__|________")
	if n == 8:
		print("   _ _     ")
		print("  |   O    ")
		print("  | _/|\_  ")
		print("  |  / \   ")
		print("__|________")	
	if n == 9:
		print("   _ _     ")
		print("  |   x    ")
		print("  | _/|\_  ")
		print("  |  / \   ")
		print("__|________")				
def main():
	print ("Hangman - World Geography Edition\n")
	f = open("countries.txt")
	countries = [line.strip() for line in open("countries.txt")]
	f.close()
	play = raw_input("Would you like to play hangman(yes/no)?  ")
	play = play.lower()
	print("\n")
	while play == "yes":
		word = random.choice(countries)
		word = word.lower()
		current = ""
		for i in word:
			if i == " ":
				current += " "
			else:
				current +="-"
		print (current)
		game = "Yes"
		wrong = 0
		guesses =[]
		while game == "Yes":
			guess = raw_input("\n\nGuess a letter or guess the word: ")
			if len(guess) == 1:
				while guess in guesses:
					print("You already guessed that letter!\n")
					printMan(wrong)
					print("\n\nGuesses")
					print(guesses)
					print("\n\n" + current)
					guess = raw_input("\n\nGuess a letter or guess the word: ")
					
			if word == (guess.lower()):
				word = word[:1].upper() + word[1:]
				print("\n" + word)
				print("You win!!!" + "\n")
				game = "NO"
				play = raw_input("Would you like to play again(yes/no)?  ")
				print("\n")
				play = play.lower()
				
			elif len(guess) == 1:
				new = ""
				guesses.append(guess)
				for i in range(len(word)):
					if guess == word[i]:
						new += guess
						
					else:
						new += current[i]
				if current == new:
					wrong += 1
				current = new
				printMan(wrong)
				print ("\n\nGuesses")
				print (guesses)
				print("\n\n" + current+ "\n")
				if wrong == 9:
					word = word[:1].upper() + word[1:]
					print("\n" + word)
					print("You lose!!!"+ "\n")
					game = "NO"
					play = input("Would you like to play again(yes/no)?  ")
					print("\n")
					play = play.lower()
					break;
				
				if current == word:
					word = word[:1].upper() + word[1:]
					print("\n" + word.title())
					print("You win!!!" + "\n")
					game = "NO"
					play = input("Would you like to play again(yes/no)?  ")
					print("\n")
					play = play.lower()
				
				
			else:
				wrong += 1
				printMan(wrong)
				print ("\n\nGuesses")
				print (guesses)
				print("\n\n" + current)
				if wrong == 9:
					word = word[:1].upper() + word[1:]
					print("\n" + word)
					print("You lose!!!"+ "\n")
					game = "NO"
					play = input("Would you like to play again(yes/no)?  ")
					print("\n")
					play = play.lower()