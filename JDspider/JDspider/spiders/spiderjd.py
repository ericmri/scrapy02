# -*- coding: utf-8 -*-
import scrapy

class jd_Spider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = (
        'http://www.jd.com/',
    )

    def parse(self, response):
        print response.body