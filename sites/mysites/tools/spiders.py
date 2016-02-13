from __future__ import unicode_literals

from dynamic_scraper.spiders.django_spider import DjangoSpider
from mysites.models import JobAd, JobWebsite, JobAdItem

class JobSpider(DjangoSpider):

	name = 'job_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(JobWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = JobAd
		self.scraped_obj_item_class = JobAdItem
		super(JobSpider, self).__init__(self, *args, **kwargs)