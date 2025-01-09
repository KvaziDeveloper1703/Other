"""
This program sorts numbers in a binary file and prints them to the console. The numbers are represented as 64-bit signed integers (signed long long).

Algorithm:

1) Sorting the Binary File:
    + Numbers are read from the file in chunks of 64-bit (8 bytes).
    + An insertion sort algorithm is applied directly within the file without loading all data into memory.
    + Numbers are moved within the file by overwriting.

2) Printing the File Contents:
    + After sorting, the program reads and prints numbers from the binary file one by one.

Input File:
+ The file numbers.bin contains a sequence of 64-bit integers.

Output:
+ The program outputs the sorted sequence of numbers to the console.

Эта программа выполняет сортировку чисел в бинарном файле и выводит их на экран. Числа представлены в формате 64-битных целых чисел (signed long long).

Алгоритм:

1) Сортировка бинарного файла:
    + Числа считываются из файла блоками по размеру 64-битного числа (8 байт).
    + Используется модификация алгоритма вставок (insertion sort) для сортировки чисел прямо в файле, без загрузки всех данных в память.
    + Числа перемещаются внутри файла путем перезаписи.

2) Вывод содержимого файла:
    + После сортировки программа считывает и выводит числа из бинарного файла по одному числу за раз.

Входной файл:
+ Файл numbers.bin содержит последовательность 64-битных целых чисел.

Вывод:
+ На экран выводится последовательность чисел, отсортированная по возрастанию.
"""

import struct

def sort_binary_file(filename):
    num_size = struct.calcsize('q')

    with open(filename, "r+b") as file:
        file.seek(0, 2)
        file_size = file.tell()
        count =file_size // num_size
    
        for i in range (1, count):
            file.seek(i * num_size, 0)
            current = struct.unpack('q', file.read(num_size))[0]

            j = i-1

            while j >= 0:
                file.seek(j*num_size)
                previous_number = struct.unpack('q', file.read(num_size))[0]

            if previous_number > current:
                file.seek((j+1)*num_size)
                file.write(struct.pack('q', previous_number))
                j = j-1
            else:
                break

            file.seek((j+1)*num_size)
            file.write(struct.pack('q', current))

def print_binary_file(filename):
    with open(filename, 'rb') as file:
        num_size = struct.calcsize('q') # 64
        chunk=file.read()
        while chunk:
            number = struct.unpack('q', chunk)[0]
            print(number, end=" ")
            chunk=file.read()

filename = "numbers.bin"

sort_binary_file(filename)

print_binary_file(filename)