"""
Prints integers from 1 to 100. Multiples of three print "Fizz",
multiples of five print "Buzz". Multiples of both three and five print "FizzBuzz"
"""

def fizzbuzz():
    for i in range(1,101):
        if (i % 3 == 0) and (i % 5 == 0):
            print(f"Index({i}): FizzBuzz")
        elif i % 3 == 0:
            print(f"Index({i}): Fizz")
        elif i % 5 == 0:
            print(f"Index({i}): Buzz")
        else:
            print(f"Index({i}): {i}")
