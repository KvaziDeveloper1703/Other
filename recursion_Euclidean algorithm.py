"""
Write a function gcd(a, b) that computes the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.

Steps:
+ If b is 0, return a as the GCD.
+ Otherwise, recursively call gcd(b, a % b) until b becomes 0.

Example:
For num1 = 48 and num2 = 18, the output will be:
"The GCD of 48 and 18 is 6"

Напишите функцию gcd(a, b), которая вычисляет наибольший общий делитель (НОД) двух целых чисел a и b с использованием алгоритма Евклида.

Шаги:
+ Если b равно 0, вернуть a как НОД.
+ Иначе рекурсивно вызвать gcd(b, a % b), пока b не станет 0.

Пример:
Для num1 = 48 и num2 = 18 вывод будет:
"НОД чисел 48 и 18 равен 6"
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")