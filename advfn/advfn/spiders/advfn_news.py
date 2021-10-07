import scrapy

#url = ['https://br.advfn.com/noticias/PAPERBR/2021/artigo/86208492']

class AdvfnNewsSpider(scrapy.Spider):
    name = 'advfn_news'    
    start_urls = url#['https://br.advfn.com/noticias/PAPERBR/2021/artigo/86208492']

    def parse(self, response):
        #start_urls = ['https://br.advfn.com/noticias/PAPERBR/2021/artigo/86208492']

        news = response.xpath("//article/div[@class='post-content post-dymamic']/p").getall()

        yield{
            'news' : news
        }
        
