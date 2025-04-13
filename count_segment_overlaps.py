"""
This program calculates the number of segments overlapping with each given time interval. It takes time intervals as input via standard input and determines how many other segments overlap with each segment.

Algorithm:
1) Input:
    + The first line contains the number of segments n;
    + The next n lines specify the start and end points of each segment in the format start end.

2) Data Processing:
    + For each segment, two events are created: a start ("start") and an end ("end") with the segment's index;
    + All events are sorted by coordinate. For events with the same coordinate, end events are processed first.

3) Overlap Calculation:
    + Iterating through the sorted events, active starts and ends of segments are counted;
    + For each segment, the result is calculated as the difference between the total number of segments and the sum of active starts and ends.

4) Output:
    + The program outputs a string where each element corresponds to the number of overlaps for the respective segment.

Эта программа вычисляет количество сегментов, пересекающихся с каждым заданным временным отрезком. Программа принимает временные интервалы через стандартный ввод и для каждого отрезка определяет число других отрезков, с которыми он пересекается.

Алгоритм работы:
1) Ввод данных:
    + Первой строкой задается число отрезков n;
    + Следующие n строк содержат начало и конец каждого отрезка в формате start end.

2) Обработка данных:
    + Для каждого отрезка создаются два события: начало ("start") и конец ("end") с указанием индекса отрезка;
    + Все события сортируются по координатам. Для событий с одинаковыми координатами события конца обрабатываются раньше.

3) Подсчет пересечений:
    + Итерируя по отсортированным событиям, подсчитываются активные начала и концы отрезков;
    + Для каждого отрезка результат вычисляется как разница между общим числом отрезков и суммой текущих активных началов и концов.

4) Вывод результата:
    + Программа выводит строку, где каждый элемент соответствует числу пересечений для соответствующего отрезка.
"""

import sys

def count_overlapping_segments(n, intervals):

    events = []
    for i, (start, end) in enumerate(intervals):
        events.append((start, 'start', i))
        events.append((end, 'end', i))

    events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else 1))

    active = set()
    result = [0] * n

    for coord, typ, idx in events:
        if typ == 'start':
            for other in active:
                result[other] += 1
                result[idx] += 1
            active.add(idx)
        else:
            active.remove(idx)

    return result

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    intervals = [tuple(map(int, line.split())) for line in data[1:]]

    result = count_overlapping_segments(n, intervals)

    print(" ".join(map(str, result)))