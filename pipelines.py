# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .settings import IMAGES_STORE
import  os
from  scrapy.pipelines.images import ImagesPipeline
class LolImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs=super(LolImagesPipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item=item

        return  request_objs
    def file_path(self, request, response=None, info=None):
        path=super(LolImagesPipeline,self).file_path(request,response,info)

        category=request.item.get('heroname') #名字
        images_store=IMAGES_STORE #路径
        category_path=os.path.join(images_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name=path.replace('full/','')
        image_path=os.path.join(category_path,image_name) #路径 文件夹名字

        return  image_path

class WangZheImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs=super(WangZheImagesPipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item=item

        return  request_objs
    def file_path(self, request, response=None, info=None):
        path=super(WangZheImagesPipeline,self).file_path(request,response,info)

        category=request.item.get('cname') #名字
        images_store=IMAGES_STORE #路径
        category_path=os.path.join(images_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name=path.replace('full/','')
        image_path=os.path.join(category_path,image_name) #路径 文件夹名字

        return  image_path





