import logging
from schedule import scheduler


logger = logging.getLogger(f'bot.{__name__}')


def remove_job(user_id):

    logger.info('Remove job from schedule')
    logger.debug(f'Remove job for user with user_id: {user_id}')

    job_list = scheduler.get_jobs()

    for job in job_list:

        logger.debug(f'Job with id: {job.id}, name: {job.name}, kwargs["user_id"]: {job.kwargs['user_id']}')

        if job.name == 'auto_send_msg' and job.kwargs['user_id'] == user_id:
            scheduler.remove_job(job.id)
            logger.debug(f'Removed job with id: {job.id}, name: {job.name}, kwargs["user_id"]: {job.kwargs['user_id']}')
