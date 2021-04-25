#! /usr/bin/env python3.7
# Write a program that prints the numbers from 1 - 100. For each multiple of three print "Fizz" instead of the number. 
# For multiples of five print "Buzz" instead of the number. If a number is a multiple of three and five then print "FizzBuzz".
# Solving this problem requires 2 key components: looping and conditionals.

upper_number = int(input("How many value should we process: "))

for number in range(1, upper_number + 1):
    pass
    if number % 5 == 0 and number % 3 == 0:
        print("Fizzbuzz")
    elif number % 5 == 0:
        print("Fizz")
    elif number % 3 == 0:
        print("Buzz")
    else:
        print(number)
