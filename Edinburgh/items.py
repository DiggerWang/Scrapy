# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class ProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    name_in = MapCompose()
    name_out = Join()

    price_in = MapCompose()


class EdinburghItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    programme = scrapy.Field()
    description = scrapy.Field(input_processor=MapCompose(),
                               output_processor=Join('\n'))
    Compulsory_Courses = scrapy.Field(input_processor=MapCompose(),
                                      output_processor=Join('\n'))
    Option_Courses = scrapy.Field(input_processor=MapCompose(),
                                  output_processor=Join('\n'))
    learning_outcomes = scrapy.Field(input_processor=MapCompose(),
                                     output_processor=Join('\n'))
    career_opportunities = scrapy.Field(input_processor=MapCompose(),
                                        output_processor=Join('\n'))
    bachelor_requirements = scrapy.Field(input_processor=MapCompose(),
                                         output_processor=Join('\n'))
    language_requirements = scrapy.Field(input_processor=MapCompose(),
                                         output_processor=Join('\n'))
    application_deadlines = scrapy.Field(input_processor=MapCompose(),
                                         output_processor=Join('\n'))
    full_time_fee = scrapy.Field(input_processor=MapCompose(),
                                 output_processor=Join('\n'))

