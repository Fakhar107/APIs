# Hidden APIs with Scrapy - easy JSON data extraction
# https://www.youtube.com/watch?v=xjieRVnuPcQ&t=68s


import scrapy


class GlassSpider(scrapy.Spider):
    name = "glass"
    allowed_domains = ["www.sunglasshut.com"]
    start_urls = ["https://21ogkm5th5-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.17.0)%3B%20Browser"]

    def parse(self, response):
        print(response.body[:500])

