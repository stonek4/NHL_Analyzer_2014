import scrapy
from tutorial.items import DMozItem2
from scrapy.contrib.exporter import CsvItemExporter

class DmozSpider2(scrapy.Spider):
  name = "dmoz2"
  allowed_domains = ["nhl.com"]
  start_urls = ['http://www.nhl.com/stats/player?fetchKey=20152ALLGAGAll&pg=%s' % page for page in xrange(1,3)]

  def parse(self, response):
    for player in response.xpath('//tbody/tr'):
      item = DMozItem2()
      item['Player'] = player.xpath('td[2]/a/text()').extract()
      item['Team'] = player.xpath('td[3]/a/text()').extract()
      item['GP'] = player.xpath('td[4]/text()').extract()
      item['GS'] = player.xpath('td[5]/text()').extract()
      item['W'] = player.xpath('td[6]/text()').extract()
      item['L'] = player.xpath('td[7]/text()').extract()
      item['OT'] = player.xpath('td[8]/text()').extract()
      item['SA'] = player.xpath('td[9]/text()').extract()
      item['GA'] = player.xpath('td[10]/text()').extract()
      item['GAA'] = player.xpath('td[11]/text()').extract()
      item['Sv'] = player.xpath('td[12]/text()').extract()
      item['SvPerc'] = player.xpath('td[13]/text()').extract()
      item['SO'] = player.xpath('td[14]/text()').extract()
      item['G'] = player.xpath('td[15]/text()').extract()
      item['A'] = player.xpath('td[16]/text()').extract()
      item['PIM'] = player.xpath('td[17]/text()').extract()
      item['TOI'] = player.xpath('td[18]/text()').extract()
      item['Fantasy'] = "0"
      yield item