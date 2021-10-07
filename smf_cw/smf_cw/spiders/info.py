import scrapy
from scrapy.crawler import CrawlerProcess


class InfoSpider(scrapy.Spider):
    name = 'info'
    
    start_urls = ['https://www.infomoney.com.br/ultimas-noticias/']
    #headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

    def parse(self, response):
        pass
        #for i in response.xpath("//div[@class='row py-3 item']"):
        #    header = i.xpath(".//div/span[@class='hl-title hl-title-2']//text()").getall()
        #    #print(header)

       #     yield{
       #         'header' : header
       #     }

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(InfoSpider)
    process.start()
#duck duck go
#page robot


#col-md-9 col-lg-8 col-xl-6 m-sm-auto m-lg-0 article-content tbl-forkorts-article
#col-md-9 col-lg-8 col-xl-6  m-sm-auto m-lg-0 article-content
#col-md-9 col-lg-8 col-xl-6  m-sm-auto m-lg-0 article-content
#col-md-9 col-lg-8 col-xl-6  m-sm-auto m-lg-0 article-content