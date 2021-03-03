"""
Output is based on User input. Multiples of three print "Fizz",
multiples of five print "Buzz". Multiples of both three and five print "FizzBuzz"
"""

class Fizzbuzz:

    def __init__(self):
        self.__loop = True
        self.__count_fizz = 0
        self.__count_buzz = 0
        self.__count_fizzbuzz = 0
        self.__count_integer = 0

    def prompt(self):
        while self.__loop:
            try:
                self.min = int(input("Enter the starting integer: "))
                self.max = int(input("Enter the ending integer: "))
                assert self.max > self.min

                self.__loop = False

            except ValueError:
                print("Please enter valid integer values only.")
            except AssertionError:
                print("Try again! Please make sure the ending integer is greater than the starting.")
            except:
                print("Oops! Some problem has occured.")

        self.checker()
                
    def checker(self):
        for i in range(self.min,self.max + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                self.__count_fizzbuzz += 1
                print(f"Index({i}): FizzBuzz")
            
            elif (i % 3 == 0):
                self.__count_fizz += 1
                print(f"Index({i}): Fizz")
            
            elif (i % 5 == 0):
                self.__count_buzz += 1
                print(f"Index({i}): Buzz")
            
            else:
                self.__count_integer += 1
                print(f"Index({i}): {i}")

        self.totals()

    def totals(self):
        print("---------------------------------------------------")
        print(f"| Fizz: {self.__count_fizz} | Buzz: {self.__count_buzz} | FizzBuzz: {self.__count_fizzbuzz} | Integer: {self.__count_integer} |")
        print("---------------------------------------------------")
