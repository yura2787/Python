

import functions

marks_in_school = [
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [12, 12, 10, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
    [5, 6, 7, 10],
]

for students_marks in marks_in_school:
    functions.send_unhappy_sms(student_marks=students_marks)
    functions.send_bad_marks_to_parents(student_marks=students_marks)