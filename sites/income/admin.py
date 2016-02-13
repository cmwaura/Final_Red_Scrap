from __future__ import unicode_literals

from django.contrib import admin
from .models import IncomeWebsite, IncomeDepo


# Register your models here.
class IncomeWebsiteAdmin(admin.ModelAdmin):
	list_display= ('id', 'title', 'url', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True


class IncomeDepoAdmin(admin.ModelAdmin):
	list_display = ('id', 'jobtitle', 'salary',)
	raw_id_fields = ('checker_runtime',)


admin.site.register(IncomeWebsite, IncomeWebsiteAdmin)
admin.site.register(IncomeDepo, IncomeDepoAdmin)