from __future__ import unicode_literals
from django.contrib import admin
from .models import JobAd, JobWebsite


class JobWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url_', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class JobAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'company', 'location','url_',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True

admin.site.register(JobWebsite, JobWebsiteAdmin)
admin.site.register(JobAd, JobAdAdmin)