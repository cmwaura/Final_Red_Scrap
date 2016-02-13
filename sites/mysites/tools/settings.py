import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","sites.settings")

BOT_NAME = "red_scrap"

SPIDER_MODULES = ["dynamic_scraper.spiders", "mysites.tools"]
USER_AGENT = '%s/%s' %(BOT_NAME, '1.0')

ITEM_PIPELINES = {
	'dynamic_scraper.pipelines.ValidationPipeline':400,
	'mysites.tools.pipelines.DjangoWriterPipeline': 800,
}