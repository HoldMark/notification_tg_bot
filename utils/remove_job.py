from schedule import scheduler


def remove_job(user_id):

    job_list = scheduler.get_jobs()

    for job in job_list:

        if job.name == 'auto_send_msg' and job.kwargs['user_id'] == user_id:

            scheduler.remove_job(job.id)
