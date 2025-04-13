"""
Write a function factorial(n) that calculates the factorial of a non-negative integer n.
+ The factorial is only defined for non-negative integers. If n is negative, raise a ValueError with the message: "Factorial is defined only for non-negative integers!";
+ The factorial of 0 or 1 is 1;
+ For n > 1, calculate the factorial recursively as n×factorial(n−1).

Example:
Input: n = 5
Output: "The factorial of 5 is 120"

Напишите функцию factorial(n), которая вычисляет факториал неотрицательного целого числа n.
+ Факториал определён только для неотрицательных целых чисел. Если n отрицательное, выбросить ValueError с сообщением: "Factorial is defined only for non-negative integers!";
+ Факториал числа 0 или 1 равен 1;
+ Для n > 1 вычислять факториал рекурсивно как n×factorial(n−1).

Пример:
Ввод: n = 5
Вывод: "Факториал числа 5 равен 120"
"""

def factorial(n):
    if n < 0:
        raise ValueError("The factorial is defined only for non-negative numbers!")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
print(f"Factorial of {number} is equal to {factorial(number)}")