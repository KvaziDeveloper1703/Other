"""
This program calculates how much time during the day all events overlap, given a list of time intervals. The program processes input via standard input and computes the total time of overlap for all events.

Algorithm:
1) Input:
    + The first line contains the number of events n;
    + The next n lines describe the time intervals of each event in the format h1 m1 s1 h2 m2 s2 (hours, minutes, seconds of the start and end times).

2) Time Processing:
    + For each event, the start and end times are converted to seconds using the parse_time function;
    + If the start time is later than the end time, the event spans midnight, and its time is split into two intervals: up to the end of the day and from the start of the day to the event's end.

3) Sorting Events:
    + Each event adds points of state change: start (+1) and end (-1);
    + The points are sorted by time.

4) Overlap Calculation:
    + The sorted events are iterated over, and the current number of active events is tracked;
    + If the number of active events equals the maximum possible (n), the time is accumulated.

5) Output:
    + The total time (in seconds) when all events overlap is printed.

Эта программа определяет, сколько времени в течение дня все события накладываются друг на друга, учитывая список событий, заданных во временных промежутках. Программа обрабатывает данные через стандартный ввод и вычисляет суммарное время пересечения всех событий.

Алгоритм работы:
1) Ввод данных:
    + Первой строкой задается число событий n;
    + Следующие n строк описывают временные промежутки каждого события в формате h1 m1 s1 h2 m2 s2 (часы, минуты, секунды начала и конца).

2) Обработка времени:
    + Для каждого события начало и конец переводятся в секунды с помощью функции parse_time;
    + Если начало позже конца, событие пересекает полночь, и время разделяется на два интервала: до конца суток и от начала суток до конца события.

3) Сортировка событий:
    + Каждое событие добавляет точки изменения состояния: начало (+1) и конец (-1);
    + Точки сортируются по времени.

4) Вычисление перекрытия:
    + Итерируется список событий, подсчитывается текущее число активных событий;
    + Если активных событий максимально возможное количество (n), суммируется время.

5) Вывод результата:
    + Выводится общее время (в секундах), когда все события накладываются друг на друга.
"""

import sys

def parse_time(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def main():
    input = sys.stdin.read
    data = input().splitlines()

    number_of_events = int(data[0])
    timeline_events = []

    for i in range(1, number_of_events + 1):
        h1, m1, s1, h2, m2, s2 = map(int, data[i].split())
        start_time = parse_time(h1, m1, s1)
        end_time = parse_time(h2, m2, s2)

        if start_time == end_time:
            timeline_events.append((0, 1))
            timeline_events.append((86400, -1))
        elif start_time < end_time:
            timeline_events.append((start_time, 1))
            timeline_events.append((end_time, -1))
        else:
            timeline_events.append((start_time, 1))
            timeline_events.append((86400, -1))
            timeline_events.append((0, 1))
            timeline_events.append((end_time, -1))

    timeline_events.sort(key=lambda event: (event[0], event[1]))

    current_active = 0
    max_active_required = number_of_events
    last_time_point = 0
    total_full_overlap_time = 0

    for current_time, change in timeline_events:
        if current_active == max_active_required:
            total_full_overlap_time += current_time - last_time_point
        current_active += change
        last_time_point = current_time

    print(total_full_overlap_time)

if __name__ == "__main__":
    main()