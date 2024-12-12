from functions import send_unhappy_sms
# from functions import send_unhappy_sms
import functions

MIN_SUCCESS_MARK = 11
MIN_PARENTS_SATISFY = 8

my_marks = [9, 10, 6, 12, 5]

is_contain_6 = 6 in my_marks
is_not_contain = 5 not in my_marks

is_contain_a = 'a' in 'data'
is_contain_b = 'b' in 'data'
is_contain_da = 'da' in 'data'
message = 'Я відвідав на вихідних Одесу, Харків та Київ - ох і тиждень був!!!'
is_odesa_visited = 'одес' in message.lower()

if is_odesa_visited:
    print('Send SMS: pay your debt!!!')

# for mark in my_marks:
#     print(mark)
#     if mark < MIN_SUCCESS_MARK:
#         print(f'Send SMS: say something to your child, they got {mark}')
#         break
#     print(1111111)
functions.send_unhappy_sms(student_marks=my_marks)
functions.send_unhappy_sms(student_marks=[11, 2])

bad_marks = []
for mark in my_marks:
    if mark < MIN_PARENTS_SATISFY:
        bad_marks.append(mark)

print('bad marks', len(bad_marks))

letters_over_comma = ', '.join('string')
print(letters_over_comma)

students1 = ['Andrew', 'Alex', 'Marta']
students_over_comma = ', '.join('students')
print(letters_over_comma)

if bad_marks:
    print(bad_marks)
    bad_marks_in_string = ', '.join(map(str, bad_marks))
    print(f'Send SMS: your child has got next bad marks: {bad_marks_in_string}')
else:
    print(f'Send SMS: your child is genius')

print('end loop')
