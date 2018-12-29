# -*- coding: utf-8 -*-
import scrapy


class FreedommobileSpyderSpider(scrapy.Spider):
    name = 'freedomMobile_spyder'
    allowed_domains = ['https://www.freedommobile.ca/plans-and-devices/mobile-devices']
    start_urls = ['http://https://www.freedommobile.ca/plans-and-devices/mobile-devices/']

    def parse(self, response):
        pass
