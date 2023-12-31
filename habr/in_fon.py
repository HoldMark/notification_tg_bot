import time
from celery import Celery

app = Celery('myapp', broker='sqla+sqlite:///example.sqlite')


@app.task
def generate_report_task(arg1, arg2):
    print('start generating report')
    time.sleep(10)
    print('Report generated')


app.start()
generate_report_task.call()
