# -*- coding: utf-8 -*-
import scrapy


class TechcrunchSpiderSpider(scrapy.Spider):
    #name of the spider
    name = 'techcrunch_spider'

    #list of allowed domains
    allowed_domains = ['techcrunch.com/feed/']

    #starting url for scraping
    start_urls = ['http://techcrunch.com/feed/']

    #setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : 'tmp/techcrunch.csv'
    }

    def parse(self, response):
        pass
