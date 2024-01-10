from schedule import scheduler


async def remove_msgs_today(*args, **kwargs):
    job_list = scheduler.get_jobs()

    for i in job_list:
        if i.name == 'auto_send_msg':
            scheduler.remove_job(i.id)
