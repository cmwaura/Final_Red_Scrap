import datetime
from haystack import indexes
from .models import JobAd


class JobAdIndex(indexes.SearchIndex, indexes.Indexable):
	'''
	In this case we are creating a search index basesd in the django models
	of JobAd. Why JobAd? because that is where all the new jobs that we have 
	scraped are stored. In this way anybody can search for a particular job and
	get a good estimate result. It inherits from haystack indexes and from the 
	class SearchIndex and Indexable, gets the relevant model and returns then 
	JobAd.
	'''
	
	text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/mysites/jobad_text.txt")
	company = indexes.CharField(model_attr='company')
	location = indexes.CharField(model_attr='location')

	def get_model(self):
		return JobAd
		