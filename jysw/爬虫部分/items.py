# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JyswItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class XueqiuItem(scrapy.Item):
    symbol = scrapy.Field()
    name = scrapy.Field()
    current = scrapy.Field()
    percent = scrapy.Field()
    market_capital = scrapy.Field()
    pe_ttm = scrapy.Field()
