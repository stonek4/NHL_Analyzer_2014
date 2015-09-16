import scrapy
from tutorial.items import DMozItem
from scrapy.contrib.exporter import CsvItemExporter

class DmozSpider(scrapy.Spider):
  name = "dmoz"
  allowed_domains = ["nhl.com"]
  start_urls = ['http://www.nhl.com/stats/player?fetchKey=20152ALLSASAll&pg=%s' % page for page in xrange(1,20)]

  def parse(self, response):
    for player in response.xpath('//tbody/tr'):
      item = DMozItem()
      item['Player'] = player.xpath('td[2]/a/text()').extract()
      item['Team'] = player.xpath('td[3]/a/text()').extract()
      item['Pos'] = player.xpath('td[4]/text()').extract()
      item['GP'] = player.xpath('td[5]/text()').extract()
      item['G'] = player.xpath('td[6]/text()').extract()
      item['A'] = player.xpath('td[7]/text()').extract()
      item['P'] = player.xpath('td[8]/text()').extract()
      item['PlusMin'] = player.xpath('td[9]/text()').extract()
      item['PIM'] = player.xpath('td[10]/text()').extract()
      item['PPG'] = player.xpath('td[11]/text()').extract()
      item['PPP'] = player.xpath('td[12]/text()').extract()
      item['SHG'] = player.xpath('td[13]/text()').extract()
      item['SHP'] = player.xpath('td[14]/text()').extract()
      item['GW'] = player.xpath('td[15]/text()').extract()
      item['OT'] = player.xpath('td[16]/text()').extract()
      item['S'] = player.xpath('td[17]/text()').extract()
      item['SPerc'] = player.xpath('td[18]/text()').extract()
      item['TOI'] = player.xpath('td[19]/text()').extract()
      item['Shift'] = player.xpath('td[20]/text()').extract()
      item['FO'] = player.xpath('td[21]/text()').extract()  
      item['Fantasy'] = "0"
      yield item