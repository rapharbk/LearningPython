secret_word = "overwatch"
guess = ""
guess_count = 0
guess_limit = 5
out_off_guesses = False


while guess != secret_word and not(out_off_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_off_guesses = True


if out_off_guesses:
    print("Out of guesses, You lose")
else:
    print("you win!")