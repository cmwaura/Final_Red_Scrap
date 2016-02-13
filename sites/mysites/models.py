from __future__ import unicode_literals


from django.db import models
from django.db.models.signals import pre_delete
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.dispatch import receiver
# Create your models here.



class JobWebsite(models.Model):
	'''
	in this situation this is the job website that we will be scraping from. So for instance if we are looking for all 
	the business analyst postions from indeed.com this particular django models wll specify what website is nessecary for
	which particular job. 
	It borrows from thenm django class models.Model to do the job.
	The scraper variable is the actual scraper that will borrow from the dynamic_scraper modules and is responsible 
	for using scrapy functions to scrape whatever website we desire.
	The scraper_runtime is as the title suggest. It borrows from the SchedulerRuntime class of the dynamic_scraper modulesd
	'''

	title = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)



class JobAd(models.Model):
	'''
	This particular class is concerned with receiving all the scraped material once the job is done. For instance if we are scraping 
	business analyst positions from a company in mountain view then what we expect is that:
	title = Jr Business Analyst
	url = www.company.com/careers.html (or something similar)
	description = "this is a junior level position for college graduates that require 10 years of freaking experience. We dont care 
	that you are only 23 you must have started working snce you were 12. actually scratch that, by the time you were conceived if you 
	didnt know what batch processing was dont even bother applying because we will not consider you.
	company = company
	location = virtual location with virtual address
	'''

	job_website = models.ForeignKey(JobWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	company = models.CharField(max_length=200)
	location = models.CharField(max_length=300)

	def __str__(self):
		return self.title


class JobAdItem(DjangoItem):
	'''
	this is a scrapy requirement for all results in the scrapy instance to be saved in the sqlite/Postgresql database in the 
	django database.
	'''

	django_model = JobAd


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
	if isinstance(instance, JobWebsite):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()

	if isinstance(instance, JobAd):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)
