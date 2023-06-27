#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>=1:
        print(f"{i}")
        i-=1
    print("Happy New Year!")

def square_integers(int_list):
    ints_squared=[]
    for num in int_list:
        ints_squared.append(num*num)
    return ints_squared

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
