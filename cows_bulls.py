#Autor: antimonious
#Datum: 27.5.2023.

import numpy as np

possible_numbers = list(np.arange(123, 9877, 1))

def format_guess(number):
    return str(number).rjust(4, '0')

def guesser():
    global possible_numbers
    
    if len(possible_numbers) == 1:
        return possible_numbers[0]
    
    median = int(np.median(possible_numbers))
    
    if median in possible_numbers:
        return median
    
    mean = int(np.mean(possible_numbers))
    flag = False
    if mean == median:
        flag = True

    guess = median
    increment = 1

    if mean < median or flag:
        while True:
            if guess + increment in possible_numbers:
                return guess + increment
            elif guess - increment in possible_numbers:
                return guess - increment
            increment += 1

    while True:
        if guess - increment in possible_numbers:
            return guess - increment
        elif guess + increment in possible_numbers:
            return guess + increment
        increment += 1

def guess_normal():
    global possible_numbers
    
    bulls = list(np.zeros(len(possible_numbers)))
    cows = list(np.zeros(len(possible_numbers)))
    for i in range(len(possible_numbers)):
        check = format_guess(possible_numbers[i])
        for j in range(len(possible_numbers)):
            check_check = format_guess(possible_numbers[j])
            for k in range(4):
                if check[k] == check_check[k]:
                    bulls[i] += 1
                elif check[k] in check_check:
                    cows[i] += 1
    
    bull_indexes = list(np.argsort(bulls))
    for i in range(len(bulls)):
        if bulls[i] != np.max(bulls):
            bull_indexes.remove(i)
    
    if len(bull_indexes) == 1:
        return possible_numbers[bulls.index(np.max(bulls))]

    max_index = bull_indexes[0]
    for i in range(1, len(bull_indexes)):
        if cows[bull_indexes[i]] > cows[max_index]:
            max_index = bull_indexes[i]
    
    return possible_numbers[max_index]

def del_range(number, updown: bool):
    global possible_numbers
    if updown:
        possible_numbers = [item for item in possible_numbers if item < number]
    else:
        possible_numbers = [item for item in possible_numbers if item > number]

def bulls_cows(guess, bulls, cows):
    global possible_numbers
    for item in possible_numbers.copy():
        check = format_guess(item)
        bull = bulls
        cow = cows
        for i in range(4):
            if check[i] == guess[i]:
                bull -= 1
            elif check[i] in guess:
                cow -= 1
        if bull != 0 or cow != 0:
            possible_numbers.remove(item)

def main():
    global possible_numbers
    
    for item in possible_numbers.copy():
        temp = format_guess(item)
        flag = False
        for i in range(3):
            for j in range(i+1, 4):
                if temp[i] == temp[j]:
                    possible_numbers.remove(item)
                    flag = True
                    break
            if flag:
                break
    
    reply = ""
    attempts = 1
    guess = 1234
    switch = False

    while True:
        print(str(attempts)+". pokusaj")
        reply = input(format_guess(guess)+" | ")
        print("--------------------")

        if reply == "4 0":
            print(format_guess(guess)+", pogodjeno iz "+str(attempts)+" pokusaja")
            break
            
        if switch:
            if '-' in reply:
                del_range(guess, False)
            else:
                del_range(guess, True)

        else:
            reply = reply.split()
            bulls = int(reply[0])
            cows = int(reply[1])
            
            bulls_cows(format_guess(guess), bulls, cows)

        possible_numbers.sort()
        
        if not switch:
            guess = guesser()
        else:
            guess = guess_normal()
            
        switch = not switch
        attempts = attempts + 1

if __name__ == '__main__':
    main()