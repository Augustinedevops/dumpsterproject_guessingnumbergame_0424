import random
secret = random.sample(range(10), k=4)
while True:
    guess = input("Enter your guess of 4-digit: ")
    if not guess:
        break 
    elif len(guess) != 4:
        continue # why?
    else:
        d, p = 0, 0
        for i in range(4):
            if int(guess[i]) in secret:
                d += 1
                if int(guess[i]) == secret[i]:
                    p += 1
        if d==4 and p==4:
            print('Congratulations! Your guess is correct!')
            break
        else:
            print('digits guessed, correct position=', (d, p))