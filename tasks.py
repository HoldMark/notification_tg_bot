# # tasks.py
#
# from celery import Celery
# from datetime import timedelta
# import time
#
# app = Celery('tasks', broker='sqla+sqlite:///example.sqlite')
#
#
# @app.task
# def send_notification():
#     print(1)
#
#
# def schedule_notifications():
#     # Пример расписания для трех отправок
#     for i in range(3):
#         send_notification.apply_async(countdown=i * 10)
#
#
# if __name__ == '__main__':
#     app.start()
#     schedule_notifications()


# ++++++++++++++++++++

import time
from celery import Celery

app = Celery('myapp', broker='sqla+sqlite:///example.sqlite')


@app.task
def generate_report_task(arg1, arg2):
    # print('start generating report')
    # time.sleep(10)
    print('Report generated')
    my_file = open('new_file.txt', 'w+')
    my_file.close()

