# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LolItem(scrapy.Item):
    images=scrapy.Field()
    image_urls=scrapy.Field()
    heroname=scrapy.Field()

class WangZheItem(scrapy.Item):
    images=scrapy.Field()
    image_urls=scrapy.Field()
    cname=scrapy.Field()


