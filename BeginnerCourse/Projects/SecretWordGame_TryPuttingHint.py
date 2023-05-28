secret_word = "overwatch"
guess = ""
guess_count = 0
guess_limit = 5
out_off_guesses = False


while guess != secret_word and not(out_off_guesses):
    if guess_count < guess_limit:
        if guess_count == 0:
            print("Hint: It's a Game")
            guess = input("Enter guess: ")
            guess_count += 1
        elif guess_count == 1:
            print("Hint 2: Activision Blizzard Make it")
            guess = input("Enter guess: ")
            guess_count += 1
        elif guess_count == 2:
            print("Hint 3: Heros Never Dies")
            guess = input("Enter guess: ")
            guess_count += 1
        elif guess_count == 3:
            print("Hint 4: the name Mercy remember you something?")
            guess = input("Enter guess: ")
            guess_count += 1
        elif guess_count == 4:
            print("Last Hint: start with OVER and end with WATCH")
            guess = input("Enter guess: ")
            guess_count += 1
    else:
        out_off_guesses = True

if out_off_guesses:
    print("Out of guesses, You lose")
else:
    print("you win!")