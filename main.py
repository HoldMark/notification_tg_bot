from tasks import generate_report_task

generate_report_task.apply_async(args=[2, 3], countdown=10)


