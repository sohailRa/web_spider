# -*- coding: utf-8 -*-
import scrapy


class TechcrunchSpiderSpider(scrapy.Spider):
    name = 'techcrunch_spider'
    allowed_domains = ['techcrunch.com/feed/']
    start_urls = ['http://techcrunch.com/feed//']

    def parse(self, response):
        pass
