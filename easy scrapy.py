import scrapy
class MofanSpider(scrapy.Spider):
    name='mofan'
    start_url=['https://morvanzhou.github.io/']
    
    def parse(self,response):
        yield {
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"','"'),
            'url': response.url
        }
        
        urls=response.css('a::attr(href)').re(r'^/.+?/$')
        for url in urls:
            yield response.follow(url,callback=self.parse)
