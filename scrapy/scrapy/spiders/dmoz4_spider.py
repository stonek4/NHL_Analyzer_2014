import scrapy
from tutorial.items import DMozItem4
from scrapy.contrib.exporter import CsvItemExporter

class DmozSpider4(scrapy.Spider):
  name = "dmoz4"
  allowed_domains = ["fanduel.com"]
  start_urls = ['https://www.fanduel.com/e/Game/12012?tableId=11618564&fromLobby=true']

  def parse(self, response):
    for player in response.xpath('//tbody/tr'):
      item = DMozItem4()
      item['Pos'] = player.xpath('td[1]/text()').extract()
      item['Player'] = player.xpath('td[2]/div/text()').extract()
      item['FPPG'] = player.xpath('td[3]/text()').extract()
      item['PP'] = player.xpath('td[4]/text()').extract()
      item['PF'] = player.xpath('td[5]/text()').extract()
      item['PS'] = player.xpath('td[6]/text()').extract()
      yield item