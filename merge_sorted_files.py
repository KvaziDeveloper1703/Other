"""
The program merges two files with sorted numbers into a single output file while preserving the order. It reads lines from both files, compares them, writes the smaller value to the output file, and continues until all lines are processed.

Программа объединяет два файла с отсортированными числами в один выходной файл, сохраняя порядок. Она поочередно считывает строки из обоих файлов, сравнивает их, записывает меньшее значение в выходной файл и продолжает, пока все строки не будут обработаны.
"""

def merge_files(file1, file2, output_file):
    with open(file1, "r") as file1, open(file2, "r") as file2, open(output_file, "w") as output:
        line1 = file1.readline().strip()
        line2= file2.readline().strip()

    while line1 or line2:
        if line1 and line2:
            if int(line1) <= int(line2):
                output.write(line1 + '\n')
                line1 = file1.readline().strip()
            else:
                output.write(line2 + '\n')
                line2 = file2.readline().strip()
        elif line1:
            output.write(line1 + '\n')
            line1 = file1.readline().strip()
        elif line2:
            output.write(line2 + '\n')
            line2 = file2.readline().strip()

merge_files("in1.txt", "in2.txt", "output.txt")