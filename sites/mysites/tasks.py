from celery.task import task
from django.db.models import Q
from dynamic_scraper.utils.task_utils import TaskUtils
from .models import JobAd, JobWebsite

@task
def run_spiders():
	t = TaskUtils()
	# Django field lookup keyword arguments to specify which ref objects(JobWebsite)
	# to run
	kwargs = {
		'scrape_me':True,
	}
	args=(Q(name = 'Dice'),)
	t.run_spiders(JobWebsite, 'scraper', 'scraper_runtime', 'job_spider', *args, **kwargs)

@task
def run_checkers():
	t = TaskUtils()

	kwargs = {
		'check_me':True,
	}
	args=(Q(id__gt = 100),)
	t.run_checkers(JobAd, 'job_website__scraper', checker_runtime, 'job_checker', *args, **kwargs)
