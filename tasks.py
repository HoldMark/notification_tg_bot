from celery import Celery

app = Celery('myapp', broker='sqla+sqlite:///example.sqlite')


@app.task
def generate_report_task(arg1, arg2):
    print('Report generated')
    my_file = open('new_file.txt', 'w+')
    my_file.close()

