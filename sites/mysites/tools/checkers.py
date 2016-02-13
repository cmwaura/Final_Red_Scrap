from dynamic_scraper.spiders.django_checker import DjangoChecker
from  mysites.models import JobAd


class JobChecker(DjangoChecker):
	'''
	The JobChecker class inherits from the DjangoChecker class in the Dynamic Django scraper
	module hence why we imported it. The main aim of this module is checking the objects that we
	scrape mainly through the ref_object.url and see if there is any recurrence in the process. If 
	there is a recurrence the new object will be deleted to keep the integrity of the data. We will 
	also	configure a scheduler_runtime which will configure times at which the checker class will be run. 
	This is important especially after scheduling various cron jobs at which the scraper will be run.
	'''
	name = 'job_checker'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(JobAd, **kwargs)
		self.scraper = self.ref_object.job_website.scraper
		self.scheduler_runtime = self.ref_object.checker_runtime
		super(JobChecker, self).__init__(self, *args, **kwargs)
