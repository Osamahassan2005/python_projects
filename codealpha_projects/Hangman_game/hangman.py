import random

def hangman():
    #words list
    words=['python','programming','language','hangman','challenge','algorithm']

    #select any random word
    secret_word=random.choice(words)

    #empty list initialized
    guessed_letters=[]

    #total attempts
    attempts=6

    #display len of secret word by underscores
    word_progress=['_']*len(secret_word)
    print('Welcome to the Hangman Game :)')
    print(' '.join(word_progress))

    #get user input and checks
    while attempts>0 and '_' in word_progress:
        guess = input('Guess a letter: ').lower()
        if len(guess) !=1 or not guess.isalpha():
            print('Please enter a single valid letter.')
            continue
        if guess in guessed_letters:
            print("you've already guess that letter .Try again.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"Good job!,'{guess}' is in the word.")
            for i,letter in enumerate(secret_word):
                if letter == guess:
                    word_progress[i]=guess
        else:
            attempts-=1
            print(f"Sorry!,{guess} is not in the word. You have {attempts} attempts left.")

        #display current progress
        print(' '.join(word_progress))
    #result of game
    if '_' not in word_progress:
        print("Congratulation! you've guessed the word.",secret_word)
    else:
        print("You're out of attempts! the word was :",secret_word)
#run the game only if this scripte is execute directly
if __name__=='__main__':
   hangman()






