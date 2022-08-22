from random import choice
print("H A N G M A N")
lost_counter, win_counter = 0, 0


def game():
    possibilities = ["python", "java", "swift", "javascript"]
    word = choice(possibilities)
    counter = 8
    masked = ["-"]*len(word)
    used = []

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while counter !=0:
        if "".join(masked) == word:
            print(f"You guessed the word {word}!")
            print("You survived!")
            global win_counter
            win_counter +=1
            break
        print()
        print("".join(masked))
        print("Input a letter:")
        guess = input()
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if guess not in alphabet:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if guess.isalpha() == False:
            print("Please, input a single letter.")
            continue
        if guess in used:
            print("You've already guessed this letter.")
            continue

        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    masked[i] = guess
            used.append(guess)
        else:
            print("That letter doesn't appear in the word.")
            used.append(guess)
            counter-=1
        if counter == 0:
            print("You lost!")
            global lost_counter
            lost_counter +=1

            break

def menu():
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        decision = input()
        if decision not in ["play","results","exit"]:
            continue
        if decision == "play":
            game()
        if decision == "results":
            print(f"You won: {win_counter} times")
            print(f"You lost: {lost_counter} times")
        if decision == "exit":
            break
menu()


# Hello!
