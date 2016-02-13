from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_delete
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.dispatch import receiver

# Create your models here.
class IncomeWebsite(models.Model):

	title = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class IncomeDepo(models.Model):

	income_website = models.ForeignKey(IncomeWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	jobtitle = models.CharField(max_length=250)
	salary = models.IntegerField()

	def __str__(self):
		return self.jobtitle

class IncomeDepoItem(DjangoItem):

	django_model = IncomeDepo

@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
	if isinstance(instance, IncomeWebsite):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()

	if isinstance(instance, IncomeDepo):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()

pre_delete.connect(pre_delete_handler)



