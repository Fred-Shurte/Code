"""
Prints integers from 1 to 100. Multiples of three print "Fizz",
multiples of five print "Buzz". Multiples of both three and five print "FizzBuzz"
"""

for i in range (1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
