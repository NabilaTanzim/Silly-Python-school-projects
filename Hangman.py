Word = "Hangman"

strikes = 10

GuessAdd = []

done = False

while not done:
    for letter in Word:
        if letter.lower() in GuessAdd:
            print(letter, end = " ")
        else:
            print("_", end = "")

    MyGuess = input(f"You have {strikes} strikes left, Guess the later: ")
    GuessAdd.append(MyGuess.lower())
    if MyGuess.lower() not in Word.lower():
        strikes -= 1
        if strikes == 0:
            break

    done = True
    for letter in Word:
        if letter.lower() not in GuessAdd:
         done = False

if done:
    print(f"Hurray, the word is {Word}")
else:
    print("Game Over")