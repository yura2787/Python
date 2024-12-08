import logging

from pywebio.input import input as pw_input
from pywebio.output import put_text, put_success, put_error

score = 0

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

QUESTION1 = 'Юпітер'
QUESTION2 = '7'
QUESTION3 = 'Париж'
QUESTION4 = 'Алюміній'
QUESTION5 = '7'

name = pw_input('Як вас звати').title()

ques = pw_input(label='Яка планета є найбільшою у Сонячній системі?', required=True).title()
logging.info(f'Питання, введене користувачем {ques}')
is_correct_compare_ques = QUESTION1 == ques
logging.debug(f'Конкретне питання введене користувачем {is_correct_compare_ques}')
if is_correct_compare_ques:
    put_success(is_correct_compare_ques)
    score = score + 1
    logging.info(f'Питання, введене користувачем {ques}')
else:
    put_error(is_correct_compare_ques)
    score = score + 0
    logging.info(f'Питання, введене користувачемo {ques}')

ques1 = pw_input(label='Скільки континентів на Землі?', required=True)
logging.info(f'Питання, введене користувачем {ques1}')
is_correct_compare_ques1 = QUESTION2 == ques1
logging.debug(f'Конкретне питання введене користувачем {is_correct_compare_ques1}')
if is_correct_compare_ques1:
    put_success(is_correct_compare_ques1)
    score = score + 1
    logging.info(f'Питання, введене користувачем {ques1}')
else:
    put_error(is_correct_compare_ques1)
    score = score + 0
    logging.info(f'Питання, введене користувачемo {ques1}')

ques2 = pw_input(label='Як називається столиця Франції?', required=True).title()
logging.info(f'Питання, введене користувачем {ques2}')
is_correct_compare_ques2 = QUESTION3 == ques2
logging.debug(f'Конкретне питання введене користувачем {is_correct_compare_ques2}')
if is_correct_compare_ques2:
    put_success(is_correct_compare_ques2)
    score = score + 1
    logging.info(f'Питання, введене користувачем {ques2}')
else:
    put_error(is_correct_compare_ques2)
    score = score + 0
    logging.info(f'Питання, введене користувачемo {ques2}')

ques3 = pw_input(label='Який метал є основним у виробництві алюмінієвої фольги?', required=True).title()
logging.info(f'Питання, введене користувачем {ques3}')
is_correct_compare_ques3 = QUESTION4 == ques3
logging.debug(f'Конкретне питання введене користувачем {is_correct_compare_ques3}')
if is_correct_compare_ques3:
    put_success(is_correct_compare_ques3)
    score = score + 1
    logging.info(f'Питання, введене користувачем {ques3}')
else:
    put_error(is_correct_compare_ques3)
    score = score + 0
    logging.info(f'Питання, введене користувачемo {ques3}')

ques4 = pw_input(label='Скільки кольорів у веселці?', required=True)
logging.info(f'Питання, введене користувачем {ques4}')
is_correct_compare_ques4 = QUESTION5 == ques4
logging.debug(f'Конкретне питання введене користувачем {is_correct_compare_ques4}')
if is_correct_compare_ques4:
    put_success(is_correct_compare_ques4)
    score = score + 1
    logging.info(f'Питання, введене користувачем {ques4}')
else:
    put_error(is_correct_compare_ques4)
    score = score + 0
    logging.info(f'Питання, введене користувачемo {ques4}')

percent = score / 5

put_text(f'{name} у вас {score} балів а це {percent} відсотків.')
