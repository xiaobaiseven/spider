# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Pic51Item(scrapy.Item):
    # define the fields for your item here like:
    explore_name = scrapy.Field()
    image_alt = scrapy.Field()
    image_url = scrapy.Field()
    # pass
