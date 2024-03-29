
import random

with open ("words.txt") as file:
    word_bank = file.read().split()

easy_words =[]
medium_words = []
hard_words = []

def game_setup (word_bank):
    for word in word_bank:
        if len(word) > 3 and len(word) < 7:
            easy_words.append(word)
        if len(word) > 5 and len(word) < 9:
            medium_words.append(word)
        if len(word) > 7:
            hard_words.append(word)

game_setup(word_bank)

def choose_random_word(list):
    random_index = (random.randrange(0, len(list), 1))
    random_word = list[random_index]
    return random_word.lower()

def run_game():
    game_over = False
    game_board = []
    user_guesses = []
    wrong_guesses = []
    guess_count = 8

    print("\nWORD GUESS: where I know a word, and you don't! Yet...\n")

    level = input("Choose difficulty level: [E]asy [M]edium or [H]ard: " )

    if level == "e" or level == "E":
        random_word = choose_random_word(easy_words)
    elif level == "m" or level == "M":
        random_word = choose_random_word(medium_words)
    elif level == "h" or level == "H":
        random_word = choose_random_word(hard_words)

    print(f"\nYour word has {len(random_word)} letters to guess.\n")

    if len(user_guesses) == 0:
        game_board.append('_ ' * len(random_word))
        print('')
        print('')
        print(' '.join(game_board))
        print('')

    while game_over == False:
        print('')
        print(f'Remaining guesses: {guess_count}')
        print('')
        print('Wrong guesses: ' + ', '.join(wrong_guesses))
        print('')

        guess = input("Guess a letter: " )
        print('')
        legit_guess = False

        if len(guess) == 1 and guess not in wrong_guesses and guess.isalpha():
            legit_guess = True
            user_guesses.append(guess)

        while legit_guess == False:

            if len(guess) > 1:
                print("\nOne at a time, please. \n")
            elif not guess.isalpha():
                print("\nLetters only, please. \n")
            elif guess in wrong_guesses:
                print("\nYou already guessed that letter. \n")
            
            guess = input("Try again: " )
                            
            if len(guess) == 1 and guess.isalpha() and guess not in wrong_guesses:
                legit_guess = True
                user_guesses.append(guess)


        game_board = []

        for letter in random_word:
            if letter in user_guesses:
                game_board.append(letter)
            else:
                game_board.append('_')

        for guess in user_guesses:
            if guess not in random_word and guess not in wrong_guesses:
                wrong_guesses.append(guess)

        print(' '.join(game_board))

        guess_count = 8 - len(wrong_guesses)

        if guess_count == 0:
            game_over = True
            print("\nGame Over. You did not win.\n")
            print("The word was", random_word)
            print('')
        if "_" not in game_board:
            game_over = True
            print("\nGame Over. You win.\n")

        if game_over == True:
            replay = input("\nPlay again? [Y]es or [N]o way: ")
            if replay.lower() == "y":
                game_setup(word_bank)
                run_game()
            else:
                print("\nBoo.\n") 
    
run_game()
