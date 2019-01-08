from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
import sys

#if sys.version_info[0] >= 3: unicode = str

class TechCrunchArticleLoader(ItemLoader):
    default_input_processor = MapCompose(lambda s: str(s, "utf-8"), str.strip)
    default_output_processor = Join()

    title_in = MapCompose(str.strip, str.title)
    title_out = Join()

    text_in = MapCompose(str.strip)
    text_out = Join()

    tags_in = MapCompose(str.strip)
    tags_out = Join(separator=u'; ')
