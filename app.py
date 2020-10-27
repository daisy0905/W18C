numbers = [4, 7, 20, 25, 27, 33, 40, 120, 100, 80, 84, 80, 65, 67, 40]
def check_if_divisible(data):
    for number in data:
        if(number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif(number % 3 == 0):
            print("Fizz")
        elif(number % 5 == 0):
            print("Buzz")
        else: 
            print(number) 

check_if_divisible(numbers)