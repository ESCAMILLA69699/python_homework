
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        word = "".join([char if char in guesses else "_" for char in secret_word])

        print(word)

        if "_" not in word:
            return True
        else:
            return False

    return hangman_closure


secret_word = input("Enter a secret word: ")
hangman = make_hangman(secret_word)

while True:
    letter = input("Guess a letter: ")

    if hangman(letter):
        print("You guessed the word!")
        break
