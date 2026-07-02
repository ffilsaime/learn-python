#todo: Need to make this more efficient

import random
import static.hangman_words
import static.hangman_art

word_list = static.hangman_words.word_list
lives = 6

stages = static.hangman_art.stages
print(static.hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guesses = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print("You already guessed that letter")
        continue

    display = ""
    guesses.append(guess)

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}. It's not in the word. You lost one life.")

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The chosen word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
