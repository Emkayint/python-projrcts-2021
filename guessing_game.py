import random
lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']

secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
print(heart_symbol)
guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
	index = 0
	while index < len(secret_word):
		if guessed_letter == secret_word[index]:
			clue[index] = guessed_letter
		index = index+1
		
		
while lives > 0:
	print(clue)
	print('lives Left: ' + heart_symbol * lives)
	guess = input('Guess a letter or the whole words: ')
	
	if guess == secret_word:
		guessed_word_correctly=True
		break

	if guess in secret_word:
		update_clue(guess, secret_word, clue)
	else:
		print('incorrect. You loose a life')
		lives = lives -1
