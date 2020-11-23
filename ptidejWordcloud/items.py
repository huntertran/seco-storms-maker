# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WordcloudItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project_root = scrapy.Field()
    link = scrapy.Field()
    text = scrapy.Field()