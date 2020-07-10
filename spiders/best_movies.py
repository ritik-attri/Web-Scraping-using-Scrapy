# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from scrapy.utils.response import open_in_browser

class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//td[@class='titleColumn']//a")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        name=response.xpath('//div[@class="title_wrapper"]//h1//text()').get()
        imdb_rating=response.xpath('//span[@itemprop="ratingValue"]/text()').get()
        year=response.xpath('(//time)[1]/text()').get()
        genre=response.xpath('//div[@class="subtext"]/a/text()').getall()
        yield {
            'Name':name,
            'IMDB_Rating':imdb_rating,
            'Year':year,
            'Genre':genre,
        }
