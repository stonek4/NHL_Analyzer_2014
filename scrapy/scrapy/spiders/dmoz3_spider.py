import scrapy
from tutorial.items import DMozItem3
from scrapy.contrib.exporter import CsvItemExporter

class DmozSpider3(scrapy.Spider):
  name = "dmoz3"
  allowed_domains = ["nhl.com"]
  start_urls = ['http://www.nhl.com/stats/team']

  def parse(self, response):
    for player in response.xpath('//tbody/tr'):
      item = DMozItem3()
      item['Team'] = player.xpath('td[2]/a/text()').extract()
      item['GP'] = player.xpath('td[3]/text()').extract()
      item['W'] = player.xpath('td[4]/text()').extract()
      item['L'] = player.xpath('td[5]/text()').extract()
      item['OT'] = player.xpath('td[6]/text()').extract()
      item['P'] = player.xpath('td[7]/text()').extract()
      item['ROW'] = player.xpath('td[8]/text()').extract()
      item['HROW'] = player.xpath('td[9]/text()').extract()
      item['RROW'] = player.xpath('td[10]/text()').extract()
      item['PPerc'] = player.xpath('td[11]/text()').extract()
      item['GGP'] = player.xpath('td[12]/text()').extract()
      item['GAGP'] = player.xpath('td[13]/text()').extract()
      item['FA'] = player.xpath('td[14]/text()').extract()
      item['PPPerc'] = player.xpath('td[15]/text()').extract()
      item['PKPerc'] = player.xpath('td[16]/text()').extract()
      item['SGP'] = player.xpath('td[17]/text()').extract()
      item['SAP'] = player.xpath('td[18]/text()').extract()
      item['Sc1Perc'] = player.xpath('td[19]/text()').extract()
      item['Tr1Perc'] = player.xpath('td[20]/text()').extract()
      item['Ld1Perc'] = player.xpath('td[21]/text()').extract()
      item['Ld2Perc'] = player.xpath('td[22]/text()').extract()
      item['OSPerc'] = player.xpath('td[23]/text()').extract()
      item['OSBPerc'] = player.xpath('td[24]/text()').extract()
      item['FOPerc'] = player.xpath('td[25]/text()').extract()
      item['Fantasy'] = "0"
      yield item