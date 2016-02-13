from __future__ import unicode_literals
from builtins import str, object

import logging
from scrapy.exceptions import DropItem

from django.db.utils import IntegrityError
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):

	def process_item(self, item, spider):
		if spider.conf['DO_ACTION']:
			try:
				item['job_website'] = spider.ref_object

				checker_rt = SchedulerRuntime(runtime_type='C')
				checker_rt.save()
				item['checker_runtime'] = checker_rt
				item.save()
				spider.action_successful = True
				spider.log("Items saved in the DB", logging.INFO)

			except IntegrityError, e:
				spider.log(str(e), logging.ERROR)
				raise DropItem("missing attrib")
			
		
		return item
