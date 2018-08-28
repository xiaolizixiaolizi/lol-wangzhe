# -*- coding: utf-8 -*-
import scrapy
import re
import json
from ..items import LolItem
class HeroskinsSpider(scrapy.Spider):
    name = 'heroskins'
    allowed_domains = ['lol.qq.com']
    start_urls = ['http://lol.qq.com/biz/hero/champion.js']

    def parse(self, response):
        text=response.text


        js_list=re.search(r'"keys":(.*),"data"',text).group(1)
        dict_js=json.loads(js_list) #str→json

        for key ,value in dict_js.items():
            heroname=value
            hero_url='http://lol.qq.com/biz/hero/{}.js'.format(heroname)

            request=scrapy.Request(
                url=hero_url,
                callback=self.parse_heroskins,
                meta={"info":(heroname)}

            )
            yield  request

    def parse_heroskins(self,response):
        heroname=response.meta.get('info')
        text=response.text
        skins_str=re.search(r'"skins":(\[.*\]),"info"',text).group(1)
        # print(type(skins_str))

        skin_lists=json.loads(skins_str) #str→list
        picture_ids=list()

        for skin_list in skin_lists:
            id=skin_list['id']
            picture_ids.append(id)

        image_urls=list(map(lambda x:'http://ossweb-img.qq.com/images/lol/web201310/skin/big{}.jpg'.format(x),picture_ids))

        item=LolItem(heroname=heroname,image_urls=image_urls)
        yield  item













