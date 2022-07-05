def appearance(all_intervals):
    """
    Возвращает время общего присутствия ученика и
    учителя на уроке (в секундах)
    """
    counter = 0
    lesson, pupils, tutors = all_intervals.values()
    lesson_start, lesson_end = lesson[0], lesson[1]

    def filter_intervals(intervals):
        intervals_list = []
        for iv in range(0, len(intervals), 2):
            if intervals[iv] > lesson_end or \
                    intervals[iv] == intervals[iv - 1] or \
                    intervals[iv + 1] < lesson_start:
                continue
            if lesson_start > intervals[iv] and lesson_end > intervals[iv + 1]:
                intervals_list.append(range(lesson_start, intervals[iv + 1]))
            elif lesson_end < intervals[iv + 1]:
                intervals_list.append(range(intervals[iv], lesson_end))
            else:
                intervals_list.append(range(intervals[iv], intervals[iv + 1]))
        return intervals_list

    pupil_range = filter_intervals(pupils)
    tutor_range = filter_intervals(tutors)

    for t in tutor_range:
        for p in pupil_range:
            max_ = max(p[0], t[0])
            min_ = min(p[-1], t[-1]) + 1
            if max_ < min_:
                intersection = range(max(p[0], t[0]), min(p[-1], t[-1]) + 1)
                counter += max(intersection) + 1 - min(intersection)
    return counter


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                        1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                        1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009,
                        1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480,
                        1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                        1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        # assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
        print(test_answer)
