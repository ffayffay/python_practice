import random
import requests

response = requests.get("https://wordsapiv1.p.rapidapi.com/words/?random=true",
  headers={
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
    "X-RapidAPI-Key": "782ba449e5mshd7b6cca45ba21edp100f31jsna8f64ebe64a9"
  }
)


# Global
# word_bank = ['elephant', 'mississippi', 'warlord', 'skeletor', 'hashbrown', 'andromeda']
word = response.json()['word']
turns = 10
failed = 0

# def get_random_numb(n):
# 	return random.randint(0,n - 1)


# def get_random_word():
# 	random_numb = get_random_numb(len(word_bank))
# 	random_word = word_bank[random_numb]
# 	return random_word

def create_correct_string(word, letter):
	global failed
	if letter in word:
		indicies = [char for char in enumerate(word) if char[1] == letter]
		for i in indicies:
			mock[i[0]] = letter
	else:
		failed = failed + 1
		print("failed attempt: {}".format(failed))
		print("Sorry wrong guess.")

	print('\n' + str(' '.join(mock)) + '\n')
	# for char in correct_chars:
	# 	if char in letters:



# word = get_random_word()
mock = ['_' for l in word]

print("""
I have chosen a word.
You have 10 chances to guess a letter or the word.
Lets begin!
--------------------------------------------------
""")

while failed < 10:
	char = input("Guess a letter.  >")
	turns -= 1
	create_correct_string(word, char)

	if not '_' in mock:
		print('you WON in {} turns! AWESOME! WHOA! SO COOL! \n\n\n\n\n\n'.format(str((turns - 10) *-1)))
		
	if failed == 9:
		print('\n LAST TRY! \n')
	elif failed == 10:
		print("Sorry LOSER but you lost!!! The word was {}".format(word))

