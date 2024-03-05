def function_name():
    """Here you can put the actions for the function"""
    return None

def sum(num_1: float, num_2: float) -> float:
    """The function adds up two numbers.

    Args:
        num_1 (float): first number.
        num_2 (float): second number.

    Returns:
        float: The total result.
    """
    sum_value: float = num_1 + num_2
    return sum_value

print(sum(24, 10))

#Exercise number one: write a function that show the massage "Hola Mundo".

def hola_mundo() -> None:
    
    print('Hola mundo')

print(hola_mundo())

def greeting(name: str) -> None:

    greeting = f"Hi! {name}"
    print(greeting)

greeting('Estiben')    

#Type a function that receives an integer as an argument and then returns its factorial.

def factorial(integer: int) -> int:

    result = 1
    while integer > 0:
        result *= integer 
        integer -= 1
    return result

print(factorial(5))

#We can use the library: math

import math

def factorial_2(number: int) -> int:
    
    factorial = math.factorial(number)
    return factorial

print(factorial_2(5))

#Exercise number two: type a function that receives a list of numbers and returns the mean.

def mean(list: list) -> float:

    sum = 0
    for number in list:
        sum += number
    return sum / len(list)

print(mean([1,2,3,4,5,6,7,8]))   

#another way to solve the exercise is using Numpy library

import statistics

x = [1,2,3,4,5,6,7,8]
print(statistics.mean(x))

