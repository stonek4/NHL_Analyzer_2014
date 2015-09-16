# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DMozItem(scrapy.Item):
  # define the fields for your item here like:
  Player = scrapy.Field()
  Team = scrapy.Field()
  Pos = scrapy.Field()
  GP = scrapy.Field()
  G = scrapy.Field()
  A = scrapy.Field()
  P = scrapy.Field()
  PlusMin = scrapy.Field()
  PIM = scrapy.Field()
  PPG = scrapy.Field()
  PPP = scrapy.Field()
  SHG = scrapy.Field()
  SHP = scrapy.Field()
  GW = scrapy.Field()
  OT = scrapy.Field()
  S = scrapy.Field()
  SPerc = scrapy.Field()
  TOI = scrapy.Field()
  Shift = scrapy.Field()
  FO = scrapy.Field()
  Fantasy = scrapy.Field()
  
class DMozItem2(scrapy.Item):
  Player = scrapy.Field()
  Team = scrapy.Field()
  GP = scrapy.Field()
  GS = scrapy.Field()
  W = scrapy.Field()
  L = scrapy.Field()
  OT = scrapy.Field()
  SA = scrapy.Field()
  GA = scrapy.Field()
  GAA = scrapy.Field()
  Sv = scrapy.Field()
  SvPerc = scrapy.Field()
  SO = scrapy.Field()
  G = scrapy.Field()
  A = scrapy.Field()
  PIM = scrapy.Field()
  TOI = scrapy.Field()
  Fantasy = scrapy.Field()

class DMozItem3(scrapy.Item):
  Team = scrapy.Field()
  GP = scrapy.Field()
  W = scrapy.Field()
  L = scrapy.Field()
  OT = scrapy.Field()
  P = scrapy.Field()
  ROW = scrapy.Field()
  HROW = scrapy.Field()
  RROW = scrapy.Field()
  PPerc = scrapy.Field()
  GGP = scrapy.Field()
  GAGP = scrapy.Field()
  FA = scrapy.Field()
  PPPerc = scrapy.Field()
  PKPerc = scrapy.Field()
  SGP = scrapy.Field()
  SAP = scrapy.Field()
  Sc1Perc = scrapy.Field()
  Tr1Perc = scrapy.Field()
  Ld1Perc = scrapy.Field()
  Ld2Perc = scrapy.Field()
  OSPerc = scrapy.Field()
  OSBPerc = scrapy.Field()
  FOPerc = scrapy.Field()
  Fantasy = scrapy.Field()
  
class DMozItem4(scrapy.Item):
  Pos = scrapy.Field()
  Player = scrapy.Field()
  FPPG = scrapy.Field()
  PP = scrapy.Field()
  PF = scrapy.Field()
  PS = scrapy.Field()

