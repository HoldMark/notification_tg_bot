# main.py
# from tasks import app
# from tasks import schedule_notifications
#
# if __name__ == '__main__':
#     # app.start()
#     schedule_notifications()

# sqla+sqlite:///example.sqlite

from tasks import generate_report_task

# generate_report_task.delay(2, 3)
generate_report_task.apply_async(args=[2, 3], countdown=10)

# celery -A tasks worker --loglevel=info -P solo

