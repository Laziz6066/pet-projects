from time import sleep
from marketplace.parsing.parsing_products.main import assitant
import datetime


def hour_2(task):
    assitant(task)
    wait_time = datetime.timedelta(hours=1, minutes=50)
    sleep_seconds = wait_time.total_seconds()
    sleep(sleep_seconds)
    assitant('Осталось 10 минут')

    minutes_10 = datetime.timedelta(minutes=10)
    sleep_seconds_2 = minutes_10.total_seconds()
    sleep(sleep_seconds_2)
    assitant('Время закончилось, Пора отдыхать!')

    wait_r_time = datetime.timedelta(minutes=30)
    rest_time = wait_r_time.total_seconds()
    sleep(rest_time)


to_do_list = [
    # "Пора учить английский!",
    "Пора заняться пет проектом",
    "Нужно готовиться к собеседованию.",
    # "Нужно полистать Линкедин по возможности добавить статью.",
    "Нужно почитать новости об IT",
    # "Пора искать работу!"
]

if __name__ == '__main__':
    assitant('Добро пожаловать!')
    for i in to_do_list:
        print(f'{datetime.datetime.now()} - i')
        hour_2(i)




