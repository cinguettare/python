#!/usr/bin/python3


import math
import easygui as g

# Detection of prime 
def is_Prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number)+1), 2):
            if number % i == 0:
                return False
        return True
    return False

def get_Primes(number):
    while True:
        if is_Prime(number):
            yield number             # Use the characteristics of the generator to calculate
        number += 1

def count_Primes():
    total = 2
    number = int(g.enterbox("Please enter the number of prime ranges to be calculated:", "Calculation of primes"))
    for prime in get_Primes(3):      # 
        if prime < number:
            total += prime
        else:
            msg = "Prime sum is: %s " % total
            g.msgbox(msg, "Calculation of primes")
            return

if __name__ == '__main__':
    count_Primes()
    

