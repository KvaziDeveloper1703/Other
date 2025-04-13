"""
Write a function gcd(number_1, number_2) that computes the greatest common divisor (GCD) of two integers number_1 and number_2 using the Euclidean algorithm.

Steps:
+ If number_2 is 0, return number_1 as the GCD;
+ Otherwise, recursively call gcd(number_2, number_1 % number_2) until number_2 becomes 0.

Example:
For number_1 = 48 and number_2 = 18, the output will be: "The GCD of 48 and 18 is 6"

Напишите функцию gcd(number_1, number_2), которая вычисляет наибольший общий делитель (НОД) двух целых чисел number_1 и number_2 с использованием алгоритма Евклида.

Шаги:
+ Если number_2 равно 0, вернуть number_1 как НОД;
+ Иначе рекурсивно вызвать gcd(number_2, number_1 % number_2), пока number_2 не станет 0.

Пример:
Для number_1 = 48 и number_2 = 18 вывод будет: "The GCD of 48 and 18 is 6"
"""

def gcd(given_number_1, given_number_2):
    if given_number_2 == 0:
        return given_number_1
    return gcd(given_number_2, given_number_1 % given_number_2)

number_1 = 48
number_2 = 18
print(f"The GCD of {number_1} and {number_2} is {gcd(number_1, number_2)}")