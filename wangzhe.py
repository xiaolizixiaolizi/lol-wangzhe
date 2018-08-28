# -*- coding: utf-8 -*-
import scrapy
import  json
import  re
from ..items import  WangZheItem
class WangzheSpider(scrapy.Spider):
    name = 'wangzhe'
    allowed_domains = ['pvp.qq.com']
    start_urls = ['https://pvp.qq.com/web201605/js/herolist.json']
    def parse(self, response):
        info_str=response.text
        info_lists=json.loads(info_str)
        for info_list in info_lists:
            ename=info_list['ename'] #hero id 105
            cname=info_list['cname'] #hero name  廉颇
            base_url='https://game.gtimg.cn/images/yxzj/img201606/heroimg/{}/{}-bigskin-{}.jpg'.format(ename,ename,' ')
            image_urls=[re.sub(r'\s',str(i),base_url) for i in range(1,10)]
            item=WangZheItem(image_urls=image_urls,cname=cname)
            yield  item









