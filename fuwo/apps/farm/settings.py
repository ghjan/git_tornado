#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author magic, create Date: 5/16/17
"""
import os
from tornado.options import define
import random

DATABASE = dict(
    db='model',
    host='127.0.0.1',
    port=27017
)


ITEM_TAG_SETS = {
    'CATEGORY_TAGS': [
        {
            'name': u'硬装建材', 'id': 'yingzhuangjiancai', 'children': [
                {
                    'name': u'门', 'id': 'men',
                    'children': [
                        { 'name': u'进户门', 'id': 'jinhumen', 'children': [], },
                        { 'name': u'室内门', 'id': 'shineimen', 'children': [], },
                        { 'name': u'移门', 'id': 'yimen', 'children': [], },
                        { 'name': u'折叠门', 'id': 'zhediemen', 'children': [], },
                        { 'name': u'门套', 'id': 'mentao', 'children': [], },
                    ],
                },
                {
                    'name': u'窗', 'id': 'chuanghu',
                    'children': [
                        { 'name': u'平开窗', 'id': 'pingkaichuang', 'children': [], },
                        { 'name': u'推拉窗', 'id': 'tuilachuang', 'children': [], },
                        { 'name': u'观景窗', 'id': 'guanjingchuang', 'children': [], },
                        { 'name': u'飘窗', 'id': 'piaochuang', 'children': [], },
                        { 'name': u'落地窗', 'id': 'luodichuang', 'children': [], },
                        { 'name': u'装饰窗', 'id': 'zhuangshichuang', 'children': [], },
                    ],
                },
                {
                    'name': u'地面', 'id': 'dimian',
                    'children': [
                        { 'name': u'地板', 'id': 'diban', 'children': [], },
                        { 'name': u'地砖', 'id': 'dizhuan', 'children': [], },
                        { 'name': u'满铺地毯', 'id': 'manputitan', 'children': [], },
                        { 'name': u'踢脚线', 'id': 'tijiaoxian', 'children': [], },
                    ],
                },
                {
                    'name': u'墙面', 'id': 'qiangmian',
                    'children': [
                        { 'name': u'墙纸', 'id': 'qiangzhi', 'children': [], },
                        { 'name': u'墙砖', 'id': 'qiangzhuan', 'children': [], },
                        { 'name': u'乳胶漆', 'id': 'rujaioqi', 'children': [], },
                        { 'name': u'护墙板', 'id': 'huqiangban', 'children': [], },
                    ],
                },
                {
                    'name': u'天花板', 'id': 'dingmian',
                    'children': [
                        { 'name': u'吊顶', 'id': 'diaoding', 'children': [], },
                        { 'name': u'顶角线', 'id': 'dingjiaoxian', 'children': [], },
                    ],
                },
                 {
                    'name': u'背景墙类', 'id': 'beijingqianglei',
                    'children': [
                        { 'name': u'背景墙', 'id': 'beijingqiang', 'children': [], },
                        { 'name': u'电视背景墙', 'id': 'dianshibeijingqiang', 'children': [], },
                        { 'name': u'卧室背景墙', 'id': 'woshibeijingqiang', 'children': [], },
                    ],
                },
                {
                    'name': u'基本构造', 'id': 'jibengouzhao',
                    'children': [
                        { 'name': u'玄关', 'id': 'xuanguan', 'children': [], },
                        { 'name': u'柱子', 'id': 'zhuzi', 'children': [], },
                        { 'name': u'地台', 'id': 'ditai', 'children': [], },
                        { 'name': u'栏杆', 'id': 'langan', 'children': [], },
                        { 'name': u'楼梯', 'id': 'louti', 'children': [], },
                        { 'name': u'壁炉', 'id': 'bilu', 'children': [], },
                    ],
                },
                {
                    'name': u'水电', 'id': 'shuidian',
                    'children': [
                        { 'name': u'开关', 'id': 'kaiguan', 'children': [], },
                        { 'name': u'插座', 'id': 'chazuo', 'children': [], },
                        { 'name': u'电箱', 'id': 'dianxiang', 'children': [], },
                        { 'name': u'接线板', 'id': 'jiexianban', 'children': [], },
                    ],
                },
            ],
        },
        {
            'name': u'家具', 'id': 'jiaju', 'children': [
                {
                    'name': u'床类', 'id': 'chuanglei',
                    'children': [
                        { 'name': u'床', 'id': 'chuang', 'checked_for': ['woshi'], 'children': [], },
                        { 'name': u'单人床', 'id': 'danrenchuang', 'checked_for': ['woshi'], 'children': [], },
                        { 'name': u'双人床', 'id': 'shuangrenchuang', 'checked_for': ['woshi'], 'children': [], },
                        { 'name': u'高低/子母床', 'id': 'gaodizimuchuang', 'children': [], },
                        { 'name': u'儿童床', 'id': 'ertongchuang', 'children': [], },
                        { 'name': u'婴儿床', 'id': 'yingerchuang', 'children': [], },
                        { 'name': u'沙发床', 'id': 'shafachuang', 'children': [], },
                        { 'name': u'榻榻米', 'id': 'tatami', 'children': [], },
                    ],
                },
                {
                    'name': u'沙发', 'id': 'shafalei',
                    'children': [
                        { 'name': u'单人沙发', 'id': 'danrenshafa', 'children': [], },
                        { 'name': u'双人沙发', 'id': 'shuangrenshafa', 'children': [], },
                        { 'name': u'多人沙发', 'id': 'duorenshafa', 'children': [], },
                        { 'name': u'组合沙发', 'id': 'zuheshafa', 'children': [], },
                        { 'name': u'儿童沙发', 'id': 'ertongshafa', 'children': [], },
                    ],
                },
                {
                    'name': u'柜', 'id': 'guilei', 'children': [
                        { 'name': u'电视柜', 'id': 'dianshigui', 'checked_for': ['keting', 'woshi'], 'children': [], },
                        { 'name': u'衣柜', 'id': 'yigui', 'checked_for': ['woshi',], 'children': [], },
                        { 'name': u'儿童衣柜', 'id': 'ertongyigui', 'checked_for': ['ertongfang',], 'children': [], },
                        { 'name': u'床头柜', 'id': 'chuangtougui', 'checked_for': ['woshi',], 'children': [], },
                        { 'name': u'餐边柜', 'id': 'canbiangui', 'checked_for': ['canting',], 'children': [], },
                        { 'name': u'书柜', 'id': 'shugui', 'children': [], },
                        { 'name': u'储物柜', 'id': 'chuwugui', 'children': [], },
                        { 'name': u'壁柜', 'id': 'bigui', 'children': [], },
                        { 'name': u'斗柜', 'id': 'dougui', 'children': [], },
                        { 'name': u'鞋柜', 'id': 'xiegui', 'children': [], },
                        { 'name': u'酒柜', 'id': 'jiugui', 'children': [], },
                        { 'name': u'门厅/玄关柜', 'id': 'mentingxuanguangui', 'children': [], },
                        { 'name': u'角柜', 'id': 'jiaogui', 'children': [], },
                    ],
                },
                {
                    'name': u'桌', 'id': 'zhuolei',
                    'children': [
                        { 'name': u'餐桌', 'id': 'canzhuo', 'children': [], },
                        { 'name': u'餐桌椅组合', 'id': 'canzhuoyizuhe', 'children': [], },
                        { 'name': u'梳妆台/桌', 'id': 'shuzhuangtaizhuo', 'children': [], },
                        { 'name': u'书桌', 'id': 'shuzhuo', 'children': [], },
                        { 'name': u'儿童书桌', 'id': 'ertongshuzhuo', 'children': [], },
                        { 'name': u'书桌椅组合', 'id': 'shuzhuoyizuhe', 'children': [], },
                        { 'name': u'电脑桌', 'id': 'diannaozhuo', 'children': [], },
                        { 'name': u'吧台/吧椅', 'id': 'bataibayi', 'children': [], },
                        { 'name': u'麻将桌', 'id': 'majiangzhuo', 'children': [], },
                    ],
                },
                {
                    'name': u'椅/凳/榻', 'id': 'yidengta',
                    'children': [
                        { 'name': u'餐椅', 'id': 'canyi', 'children': [], },
                        { 'name': u'沙发椅', 'id': 'shafayi', 'children': [], },
                        { 'name': u'写字椅', 'id': 'xieziyi', 'children': [], },
                        { 'name': u'儿童椅', 'id': 'ertongyi', 'checked_for': ['ertongfang',], 'children': [], },
                        { 'name': u'贵妃椅', 'id': 'guifeiyi', 'children': [], },
                        { 'name': u'休闲椅', 'id': 'xiuxianyi', 'children': [], },
                        { 'name': u'沙发凳', 'id': 'shafadeng', 'children': [], },
                        { 'name': u'梳妆凳', 'id': 'shuzhuangdeng', 'children': [], },
                        { 'name': u'床尾凳', 'id': 'chuangweideng', 'children': [], },
                        { 'name': u'矮凳', 'id': 'aideng', 'children': [], },
                    ],
                },
                {
                    'name': u'架', 'id': 'jiaxianglei',
                    'children': [
                        { 'name': u'衣帽架', 'id': 'yimaojia', 'children': [], },
                        { 'name': u'鞋架', 'id': 'xiejia', 'children': [], },
                        { 'name': u'书架', 'id': 'shujia', 'children': [], },
                        { 'name': u'花架', 'id': 'haujia', 'children': [], },
                        { 'name': u'博古架', 'id': 'bogujia', 'children': [], },
                        { 'name': u'隔板/壁架', 'id': 'gebanbijia', 'children': [], },
                        { 'name': u'杂志/报刊架', 'id': 'zazhibaokanjia', 'children': [], },
                    ],
                },
                {
                    'name': u'几', 'id': 'jilei',
                    'children': [
                        { 'name': u'茶几', 'id': 'chaji', 'children': [], },
                        { 'name': u'角几/边几', 'id': 'jiaojibianji', 'children': [], },
                        { 'name': u'套几', 'id': 'taoji', 'children': [], },
                    ],
                },
            ],
        },
        {
            'name': u'厨/卫', 'id': 'chuwei',
            'children': [
                {
                    'name': u'厨房', 'id': 'chufang',
                    'children': [
                        { 'name': u'橱柜', 'id': 'chugui', 'children': [], },
                        { 'name': u'橱房配件/挂架', 'id': 'chufangpeijianguajia', 'children': [], },
                        { 'name': u'厨具', 'id': 'chuju', 'children': [], },
                        { 'name': u'餐具', 'id': 'canju', 'children': [], },
                    ],
                },
                {
                    'name': u'卫浴', 'id': 'weiyu',
                    'children': [
                        { 'name': u'坐便器', 'id': 'zuobianqi', 'children': [], },
                        { 'name': u'浴室柜', 'id': 'yushigui', 'children': [], },
                        { 'name': u'洗脸台盆', 'id': 'xiliantaipen', 'children': [], },
                        { 'name': u'花洒', 'id': 'huasa', 'children': [], },
                        { 'name': u'淋浴房', 'id': 'linyufang', 'children': [], },
                        { 'name': u'浴缸', 'id': 'yugang', 'children': [], },
                        { 'name': u'小便斗', 'id': 'xiaobiandou', 'children': [], },
                        { 'name': u'卫浴配件/挂架', 'id': 'weiyupeijianguajia', 'children': [], },
                        { 'name': u'浴霸', 'id': 'yuba', 'children': [], },
                    ],
                },
            ],
        },
        {
            'name': u'家饰', 'id': 'jiashi',
            'children': [
                {
                    'name': u'家居饰品', 'id': 'jiajushipin',
                    'children': [
                        { 'name': u'屏风/隔断', 'id': 'pingfenggeduan', 'children': [], },
                        { 'name': u'装饰摆件', 'id': 'zhuangshibaijian', 'children': [], },
                        { 'name': u'照片墙', 'id': 'zhaopianqiang', 'children': [], },
                        { 'name': u'装饰画', 'id': 'zhuangshihua', 'children': [], },
                        { 'name': u'油画', 'id': 'youhua', 'children': [], },
                        { 'name': u'花瓶', 'id': 'huaping', 'children': [], },
                        { 'name': u'鱼缸', 'id': 'yurgang', 'children': [], },
                    ],
                },
                {
                    'name': u'布艺软饰', 'id': 'buyiruanshi',
                    'children': [
                        { 'name': u'窗帘', 'id': 'chuanglian', 'children': [], },
                        { 'name': u'地毯', 'id': 'ditan', 'children': [], },
                        { 'name': u'抱枕', 'id': 'baozhen', 'children': [], },
                        { 'name': u'沙发垫', 'id': 'shafadian', 'children': [], },
                    ],
                },
                {
                    'name': u'鲜花园艺', 'id': 'xianhuayuanyi',
                    'children': [
                        { 'name': u'植物/盆景', 'id': 'zhiwupenjing', 'children': [], },
                        { 'name': u'花艺套装', 'id': 'huayitaozhuang', 'children': [], },
                    ],
                },
                {
                    'name': u'镜子', 'id': 'jingzhilei',
                    'children': [
                        { 'name': u'试衣镜', 'id': 'shiyijing', 'children': [], },
                        { 'name': u'化妆镜', 'id': 'huazhuangjing', 'children': [], },
                        { 'name': u'浴室镜', 'id': 'yushijing', 'children': [], },
                    ],
                },
                {
                    'name': u'其它家饰', 'id': 'qitajiashi',
                    'children': [
                        { 'name': u'乐器', 'id': 'yueqi', 'children': [], },
                        { 'name': u'美术用品', 'id': 'meishuyongpin', 'children': [], },
                        { 'name': u'体育器材', 'id': 'tiyuqicai', 'children': [], },
                    ],
                },
            ],
        },
        {
            'name': u'灯饰', 'id': 'dengshi',
            'children': [
                {
                    'name': u'灯具', 'id': 'dengju',
                    'children': [
                        { 'name': u'吊灯', 'id': 'diaodeng', 'children': [], },
                        { 'name': u'吸顶灯', 'id': 'xidingdeng', 'children': [], },
                        { 'name': u'台灯', 'id': 'taideng', 'children': [], },
                        { 'name': u'射灯', 'id': 'shedeng', 'children': [], },
                        { 'name': u'筒灯', 'id': 'tongdeng', 'children': [], },
                        { 'name': u'落地灯', 'id': 'luodideng', 'children': [], },
                        { 'name': u'壁灯', 'id': 'bideng', 'children': [], },
                    ],
                },
            ],
        },
        {
            'name': u'家电', 'id': 'jiadian',
            'children': [
                {
                    'name': u'冰/洗/空', 'id': 'bingxikong',
                    'children': [
                        { 'name': u'冰箱', 'id': 'bingxiang', 'children': [], },
                        { 'name': u'洗衣机', 'id': 'xiyiji', 'children': [], },
                        { 'name': u'空调', 'id': 'kongtiao', 'children': [], },
                    ],
                },
                {
                    'name': u'影音数码', 'id': 'yingyinshuma',
                    'children': [
                        { 'name': u'电视', 'id': 'dianshi', 'children': [], },
                        { 'name': u'影音设备', 'id': 'yingyinshebei', 'children': [], },
                        { 'name': u'电脑', 'id': 'diannao', 'children': [], },
                    ],
                },
                {
                    'name': u'厨房电器', 'id': 'chufangdianqi',
                    'children': [
                        { 'name': u'抽油烟机', 'id': 'chouyouyanji', 'children': [], },
                        { 'name': u'燃气灶', 'id': 'ranqizao', 'children': [], },
                        { 'name': u'电磁炉', 'id': 'diancilu', 'children': [], },
                        { 'name': u'微波炉', 'id': 'weibolu', 'children': [], },
                        { 'name': u'热水器', 'id': 'reshuiqi', 'children': [], },
                        { 'name': u'消毒柜', 'id': 'xiaodugui', 'children': [], },
                    ],
                },
                {
                    'name': u'其它家电', 'id': 'qitajiadian',
                    'children': [
                        { 'name': u'饮水机', 'id': 'yinshuiji', 'children': [], },
                    ],
                },
            ],
        },
    ],

    'AREA_TAGS': [
        {'name': u'客厅', 'id': 'keting',},
        {'name': u'餐厅', 'id': 'canting',},
        {'name': u'卧室', 'id': 'woshi',},
        {'name': u'书房', 'id': 'shufang',},
        {'name': u'儿童房', 'id': 'ertongfang',},
        {'name': u'厨房', 'id': 'chufang',},
        {'name': u'卫生间', 'id': 'weishengjian',},
        {'name': u'阳台', 'id': 'yangtai',},
        {'name': u'不限空间', 'id': 'buxiankongjian',},
    ],

    'STYLE_TAGS': [
        {'name': u'现代', 'id': 'xiandai',},
        {'name': u'欧式', 'id': 'oushi',},
        {'name': u'美式', 'id': 'meishi',},
        {'name': u'新中式', 'id': 'xinzhongshi',},
        {'name': u'新古典', 'id': 'xingudian',},
        {'name': u'田园', 'id': 'tianyuan',},
        {'name': u'地中海', 'id': 'dizhonghai',},
        {'name': u'中式', 'id': 'zhongshi',},
        {'name': u'东南亚', 'id': 'dongnanya',},
        {'name': u'混搭', 'id': 'hunda',},
    ],

    # 一下为系统保留的内部tag，若存在，则不删除
    'RESERVED_TAGS': [
        {'name': u'可定制', 'id': 'kedingzhi',},
    ],
}

ITEM_CATEGORY_SET = {
    'BASE_CATEGORY':[
        {'id': 'private',         'name': u'我的物品',          'children': [
            {'id': 'private',              'name': u'我的物品', 'children': [
                {'id': 'wodeshoucang', 'name': u'我的收藏',      'children': []},
                {'id': 'wodezuhe',         'name': u'我的组合',          'children': []},
                {'id': 'wodemoxing',      'name': u'我的模型',             'children': []},
            ]},
        ]},
    ],
    'EXTEND_CATEGORY':[

        {'id': 'menchuang',     'name': u'门窗',             'children': [
            {'id': 'men',             'name': u'门',             'children': [
                {'id': 'jinhumen',         'name': u'进户门',         'children': []},
                {'id': 'shineimen',     'name': u'室内门',         'children': []},
                {'id': 'yimen',         'name': u'移门',             'children': []},
                {'id': 'zhediemen',     'name': u'折叠门',             'children': []},
                {'id': 'mentao',         'name': u'门套',             'children': []},
            ]},
            {'id': 'chuang',         'name': u'窗',             'children': [
                {'id': 'pingkaichuang',    'name': u'平开窗',         'children': []},
                {'id': 'tuilachuang',     'name': u'推拉窗',         'children': []},
                {'id': 'guanjingchuang','name': u'观景窗',         'children': []},
                {'id': 'piaochuang',     'name': u'飘窗',             'children': []},
                {'id': 'luodichuang',     'name': u'落地窗',         'children': []},
                {'id': 'zhuangshichuang','name': u'装饰窗',         'children': []},
            ]},
        ]},

        {'id': 'yingzhuang',     'name': u'硬装',             'children': [
            {'id': 'dimian',         'name': u'地面',             'children': [
                {'id': 'diban',            'name': u'地板',             'children': []},
                {'id': 'dizhuan',        'name': u'地砖',             'children': []},
                {'id': 'manpuditan',    'name': u'满铺地毯',         'children': []},
                {'id': 'tijiaoxian',    'name': u'踢脚线',         'children': []},
            ]},
            {'id': 'qiangmian',     'name': u'墙面',             'children': [
                {'id': 'qiangzhi',        'name': u'墙纸',             'children': []},
                {'id': 'qiangzhuan',    'name': u'墙砖',             'children': []},
                {'id': 'rujiaoqi',        'name': u'乳胶漆',         'children': []},
                {'id': 'beijingqiang',    'name': u'背景墙',         'children': []},
                {'id': 'huqiangban',    'name': u'护墙板',         'children': []},
            ]},
            {'id': 'tianhuaban',     'name': u'天花板',         'children': [
                {'id': 'diaoding',        'name': u'吊顶',             'children': []},
                {'id': 'dingjiaoxian',    'name': u'顶角线',         'children': []},
            ]},
            {'id': 'beijingqianglei','name': u'背景墙类',         'children': [
                {'id': 'beijingqiang',    'name': u'背景墙',         'children': []},
                {'id': 'dsbeijingqiang','name': u'电视背景墙',         'children': []},
                {'id': 'wsbeijingqiang','name': u'卧室背景墙',         'children': []},
            ]},
            {'id': 'shuidian',         'name': u'水电',             'children': [
                {'id': 'kaiguan',        'name': u'开关',             'children': []},
                {'id': 'chazuo',        'name': u'插座',             'children': []},
                {'id': 'dianxiang',        'name': u'电箱',             'children': []},
                {'id': 'jiexianban',    'name': u'接线板',         'children': []},
            ]},
            {'id': 'qita',             'name': u'其它',             'children': [
                {'id': 'xuanguan',        'name': u'玄关',             'children': []},
                {'id': 'zhuzi',            'name': u'柱子',             'children': []},
                {'id': 'ditai',            'name': u'地台',             'children': []},
                {'id': 'langan',        'name': u'栏杆',             'children': []},
                {'id': 'louti',            'name': u'楼梯',             'children': []},
                {'id': 'bilu',            'name': u'壁炉',             'children': []},
            ]},
        ]},

        {'id': 'keting',         'name': u'客厅',             'children': [
            {'id': 'shafa',         'name': u'沙发',             'children': [
                {'id': 'duorenshafa',    'name': u'多人沙发',         'children': []},
                {'id': 'zuheshafa',        'name': u'组合沙发',         'children': []},
                {'id': 'danrenshafa',    'name': u'单人沙发',         'children': []},
                {'id': 'shuangrenshafa','name': u'双人沙发',         'children': []},
                {'id': 'shafayi',        'name': u'沙发椅',         'children': []},
                {'id': 'shafadeng',        'name': u'沙发凳',         'children': []},
            ]},
            {'id': 'ketingguilei',     'name': u'客厅柜类',         'children': [
                {'id': 'dianshigui',    'name': u'电视柜',         'children': []},
                {'id': 'xiegui',        'name': u'鞋柜',             'children': []},
                {'id': 'xuanguangui',    'name': u'门厅/玄关柜',     'children': []},
                {'id': 'jiugui',        'name': u'酒柜',             'children': []},
            ]},
            {'id': 'ketingjilei',     'name': u'客厅几类',         'children': [
                {'id': 'chaji',            'name': u'茶几',             'children': []},
                {'id': 'jiaojibianji',    'name': u'角几/边几',         'children': []},
                {'id': 'taoji',            'name': u'套几',             'children': []},
            ]},
            {'id': 'ketingjialei',     'name': u'客厅架类',         'children': [
                {'id': 'yimaojia',        'name': u'衣帽架',         'children': []},
                {'id': 'xiejia',        'name': u'鞋架',             'children': []},
                {'id': 'huajia',        'name': u'花架',             'children': []},
                {'id': 'gebanbijia',    'name': u'隔板/壁架',         'children': []},
                {'id': 'zazhibaokanjia','name': u'杂志/报刊架',     'children': []},
            ]},
            {'id': 'qita',             'name': u'其它',             'children': [
                {'id': 'dianshi',        'name': u'电视',             'children': []},
                {'id': 'chuanglian',    'name': u'窗帘',             'children': []},
                {'id': 'ditan',            'name': u'地毯',             'children': []},
                {'id': 'pingfenggeduan','name': u'屏风/隔断',         'children': []},
                {'id': 'majiangzhuo',    'name': u'麻将桌',         'children': []},
                {'id': 'aideng',        'name': u'矮凳',             'children': []},
            ]},
        ]},

        {'id': 'canting',         'name': u'餐厅',             'children': [
            {'id': 'canzhuoyi',     'name': u'餐桌椅',         'children': [
                {'id': 'canzhuo',        'name': u'餐桌',             'children': []},
                {'id': 'canyi',            'name': u'餐椅',             'children': []},
                {'id': 'canzhuoyizuhe',    'name': u'餐桌椅组合',         'children': []},
            ]},
            {'id': 'cantingguilei', 'name': u'餐厅柜类',         'children': [
                {'id': 'canbiangui',    'name': u'餐边柜',         'children': []},
                {'id': 'jiugui',        'name': u'酒柜',             'children': []},
            ]},
            {'id': 'qita',             'name': u'其它',             'children': [
                {'id': 'canju',            'name': u'餐具',             'children': []},
                {'id': 'bataibayi',        'name': u'吧台/吧椅',         'children': []},
            ]},
        ]},

        {'id': 'woshi',         'name': u'卧室',             'children': [
            {'id': 'chuanglei',     'name': u'床类',             'children': [
                {'id': 'chuang',        'name': u'床',             'children': []},
                {'id': 'danrenchuang',    'name': u'单人床',         'children': []},
                {'id': 'shuangrenchuan','name': u'双人床',         'children': []},
                {'id': 'shafachuang',    'name': u'沙发床',         'children': []},
                {'id': 'tatami',        'name': u'榻榻米',         'children': []},
            ]},
            {'id': 'woshiguilei',     'name': u'卧室柜类',         'children': [
                {'id': 'chuangtougui',    'name': u'床头柜',         'children': []},
                {'id': 'yigui',            'name': u'衣柜',             'children': []},
                {'id': 'dianshigui',    'name': u'电视柜',         'children': []},
                {'id': 'dougui',        'name': u'斗柜',             'children': []},
                {'id': 'jiaogui',        'name': u'角柜',             'children': []},
            ]},
            {'id': 'qita',             'name': u'其它',             'children': [
                {'id': 'chuanglian',    'name': u'窗帘',             'children': []},
                {'id': 'ditan',            'name': u'地毯',             'children': []},
                {'id': 'shuzhuangtai',    'name': u'梳妆台/桌',         'children': []},
                {'id': 'shuzhuangdeng',    'name': u'梳妆凳',         'children': []},
                {'id': 'huazhuangjing',    'name': u'化妆镜',         'children': []},
                {'id': 'chuangweideng',    'name': u'床尾凳',         'children': []},
                {'id': 'dianshi',        'name': u'电视',             'children': []},
            ]},]},

        {'id': 'shufang',         'name': u'书房',             'children': [
            {'id': 'shuzhuoyi',     'name': u'书桌椅',         'children': [
                {'id': 'shuzhuo',        'name': u'书桌',             'children': []},
                {'id': 'xieziyi',        'name': u'写字椅',         'children': []},
                {'id': 'diannaozhuo',    'name': u'电脑桌',         'children': []},
                {'id': 'shuzhuoyizuhe',    'name': u'书桌椅组合',         'children': []},
            ]},
            {'id': 'qita',             'name': u'其它',             'children': [
                {'id': 'shujia',        'name': u'书架',             'children': []},
                {'id': 'shugui',        'name': u'书柜',             'children': []},
                {'id': 'diannao',        'name': u'电脑',             'children': []},
                {'id': 'zazhibaokanjia','name': u'杂志/报刊架',     'children': []},
            ]},
        ]},

        {'id': 'chuwei',         'name': u'厨卫',             'children': [
            {'id': 'chufang',         'name': u'厨房',             'children': [
                {'id': 'chugui',        'name': u'橱柜',             'children': []},
                {'id': 'chufangpeijian','name': u'厨房配件/挂架',     'children': []},
                {'id': 'chuju',            'name': u'厨具',             'children': []},
                {'id': 'canju',            'name': u'餐具',             'children': []},
            ]},
            {'id': 'chufangdianqi', 'name': u'厨房电器',         'children': [
                {'id': 'chouyouyanji',    'name': u'抽油烟机',         'children': []},
                {'id': 'ranqizao',        'name': u'燃气灶',         'children': []},
                {'id': 'diancilu',        'name': u'电磁炉',         'children': []},
                {'id': 'weibolu',        'name': u'微波炉',         'children': []},
                {'id': 'reshuiqi',        'name': u'热水器',         'children': []},
                {'id': 'xiaodugui',        'name': u'消毒柜',         'children': []},
            ]},
            {'id': 'weiyu',         'name': u'卫浴',             'children': [
                {'id': 'zuobianqi',        'name': u'坐便器',         'children': []},
                {'id': 'yushigui',        'name': u'浴室柜',         'children': []},
                {'id': 'xiliantaipen',    'name': u'洗脸台盆',         'children': []},
                {'id': 'huasa',            'name': u'花洒',             'children': []},
                {'id': 'linyufang',        'name': u'淋浴房',         'children': []},
                {'id': 'yugang',        'name': u'浴缸',             'children': []},
                {'id': 'xiaobiandou',    'name': u'小便斗',         'children': []},
                {'id': 'weiyupeijian',    'name': u'卫浴配件/挂架',     'children': []},
                {'id': 'yuba',            'name': u'浴霸',             'children': []},
            ]},
        ]},

        {'id': 'ertongfang',     'name': u'儿童房',         'children': [
            {'id': 'ertongfang-xxx',     'name': u'儿童房',         'children': [
                {'id': 'ertongchuang',     'name': u'儿童床',         'children': []},
                {'id': 'gaodizimuchuang','name': u'高低/子母床',         'children': []},
                {'id': 'ertongyigui',     'name': u'儿童衣柜',         'children': []},
                {'id': 'ertongshuzhuo', 'name': u'儿童书桌',         'children': []},
                {'id': 'ertongyi',         'name': u'儿童椅',         'children': []},
                {'id': 'ertongshafa',     'name': u'儿童沙发',         'children': []},
                {'id': 'yinerchuang',     'name': u'婴儿床',         'children': []},
            ]},
        ]},

        {'id': 'dengshi',         'name': u'灯饰',             'children': [
            {'id': 'dengshi-xxx',     'name': u'灯饰',         'children': [
                {'id': 'diaodeng',         'name': u'吊灯',             'children': []},
                {'id': 'xidingdeng',     'name': u'吸顶灯',         'children': []},
                {'id': 'taideng',         'name': u'台灯',             'children': []},
                {'id': 'shedeng',         'name': u'射灯',             'children': []},
                {'id': 'tongdeng',         'name': u'筒灯',             'children': []},
                {'id': 'luodideng',     'name': u'落地灯',         'children': []},
                {'id': 'bideng',         'name': u'壁灯',             'children': []},
            ]},
        ]},

        {'id': 'jiashi',         'name': u'家饰',             'children': [
            {'id': 'jiajushipin',     'name': u'家居饰品',         'children': [
                {'id': 'pingfenggeduan','name': u'屏风/隔断',         'children': []},
                {'id': 'zhuangshijian',    'name': u'装饰摆件',         'children': []},
                {'id': 'zhaopianqiang',    'name': u'照片墙',         'children': []},
                {'id': 'zhuangshihua',    'name': u'装饰画',         'children': []},
                {'id': 'youhua',        'name': u'油画',             'children': []},
                {'id': 'huajia',        'name': u'花架',             'children': []},
                {'id': 'huaping',        'name': u'花瓶',             'children': []},
                {'id': 'yurgang',        'name': u'鱼缸',             'children': []},
            ]},
            {'id': 'buyiruanshi',     'name': u'布艺软饰',         'children': [
                {'id': 'chuanglian',    'name': u'窗帘',             'children': []},
                {'id': 'ditan',            'name': u'地毯',             'children': []},
                {'id': 'baozhen',        'name': u'抱枕',             'children': []},
                {'id': 'shafadian',        'name': u'沙发垫',         'children': []},
            ]},
            {'id': 'xianhuayuanyi', 'name': u'鲜花园艺',         'children': [
                {'id': 'zhiwupenjing',    'name': u'植物/盆景',         'children': []},
                {'id': 'huayitaozhuang','name': u'花艺套装',         'children': []},
            ]},
            {'id': 'jingzilei',     'name': u'镜子类',         'children': [
                {'id': 'shiyijing',        'name': u'试衣镜',         'children': []},
                {'id': 'huazhuangjing',    'name': u'化妆镜',         'children': []},
                {'id': 'yushijing',        'name': u'浴室镜',         'children': []},
            ]},
            {'id': 'qitajiashi',     'name': u'其它家饰',             'children': [

                {'id': 'yueqi',            'name': u'乐器',         'children': []},
                {'id': 'meishuyongpin',    'name': u'美术用品',         'children': []},
                {'id': 'tiyuqicai',        'name': u'体育器材',         'children': []},
            ]},
        ]},

        {'id': 'jiadian',         'name': u'家电',             'children': [
            {'id': 'bingxikong',     'name': u'冰/洗/空',         'children': [
                {'id': 'bingxiang',        'name': u'冰箱',             'children': []},
                {'id': 'xiyiji',        'name': u'洗衣机',         'children': []},
                {'id': 'kongtiao',        'name': u'空调',             'children': []},
            ]},
            {'id': 'yingyinshuma',     'name': u'影音数码',         'children': [
                {'id': 'dianshi',        'name': u'电视',             'children': []},
                {'id': 'yingyinshebei',    'name': u'影音设备',         'children': []},
                {'id': 'diannao',        'name': u'电脑',             'children': []},
            ]},
            {'id': 'chufangdianqi', 'name': u'厨房电器',         'children': [
                {'id': 'chouyouyanji',    'name': u'抽油烟机',         'children': []},
                {'id': 'ranqizao',        'name': u'燃气灶',         'children': []},
                {'id': 'diancilu',        'name': u'电磁炉',         'children': []},
                {'id': 'weibolu',        'name': u'微波炉',         'children': []},
                {'id': 'reshuiqi',        'name': u'热水器',         'children': []},
                {'id': 'xiaodugui',        'name': u'消毒柜',         'children': []},
            ]},
            {'id': 'qita',             'name': u'其它',             'children': [
                {'id': 'yinshuiji',        'name': u'饮水机',         'children': []},
            ]},
        ]},

        {'id': 'dingzhi',         'name': u'定制家具',             'children': [
            {'id': 'dingzhi-xxx',     'name': u'定制家具',             'children': [
                {'id': 'chugui',         'name': u'橱柜',             'children': []},
                {'id': 'zuheshafa',     'name': u'组合沙发',         'children': []},
                {'id': 'canzhuoyizuhe', 'name': u'餐桌椅组合',         'children': []},
                {'id': 'shuzhuoyizuhe', 'name': u'书桌椅组合',         'children': []},
            ]},
        ]},

        {'id': 'jiaju',     'name': u'全部家具',                 'children': [
            {'id': 'chuanglei',     'name': u'床类',             'children': [
                {'id': 'chuang',        'name': u'床',             'children': []},
                {'id': 'danrenchuang',    'name': u'单人床',         'children': []},
                {'id': 'shuangrenchuan','name': u'双人床',         'children': []},
                {'id': 'gaodizimuchuang','name': u'高低/子母床',         'children': []},
                {'id': 'ertongchuang',    'name': u'儿童床',         'children': []},
                {'id': 'yingerchuang',    'name': u'婴儿床',         'children': []},
                {'id': 'shafachuang',    'name': u'沙发床',         'children': []},
                {'id': 'tatami',        'name': u'榻榻米',         'children': []},
            ]},
            {'id': 'shafa',         'name': u'沙发',             'children': [
                {'id': 'danrenshafa',    'name': u'单人沙发',         'children': []},
                {'id': 'shuangrenshafa','name': u'双人沙发',         'children': []},
                {'id': 'duorenshafa',    'name': u'多人沙发',         'children': []},
                {'id': 'zuheshafa',        'name': u'组合沙发',         'children': []},
                {'id': 'ertongshafa',    'name': u'儿童沙发',         'children': []},
            ]},
            {'id': 'guilei',         'name': u'柜类',             'children': [
                {'id': 'dianshigui',    'name': u'电视柜',         'children': []},
                {'id': 'yigui',            'name': u'衣柜',             'children': []},
                {'id': 'ertongyigui',    'name': u'儿童衣柜',         'children': []},
                {'id': 'chuangtougui',    'name': u'床头柜',         'children': []},
                {'id': 'canbiangui',    'name': u'餐边柜',         'children': []},
                {'id': 'shugui',        'name': u'书柜',             'children': []},
                {'id': 'chuwugui',        'name': u'储物柜',         'children': []},
                {'id': 'bigui',            'name': u'壁柜',             'children': []},
                {'id': 'dougui',        'name': u'斗柜',             'children': []},
                {'id': 'xiegui',        'name': u'鞋柜',             'children': []},
                {'id': 'jiugui',        'name': u'酒柜',             'children': []},
                {'id': 'menting',        'name': u'门厅/玄关柜',     'children': []},
                {'id': 'jiaogui',        'name': u'角柜',             'children': []},
            ]},
            {'id': 'zhuolei',         'name': u'桌类',             'children': [
                {'id': 'canzhuo',        'name': u'餐桌',             'children': []},
                {'id': 'canzhuoyizuhe',    'name': u'餐桌椅组合',         'children': []},
                {'id': 'shuzhuangtai',    'name': u'梳妆台/桌',         'children': []},
                {'id': 'shuzhuo',        'name': u'书桌',             'children': []},
                {'id': 'ertongshuzhuo',    'name': u'儿童书桌',         'children': []},
                {'id': 'shuzhuoyizuhe',    'name': u'书桌椅组合',         'children': []},
                {'id': 'diannaozhuo',    'name': u'电脑桌',         'children': []},
                {'id': 'bataibayi',        'name': u'吧台/吧椅',         'children': []},
                {'id': 'majiangzhuo',    'name': u'麻将桌',         'children': []},
            ]},
            {'id': 'yidengta',         'name': u'椅凳榻',             'children': [
                {'id': 'canzhuo',        'name': u'餐桌',             'children': []},
                {'id': 'canzhuoyizuhe',    'name': u'餐桌椅组合',         'children': []},
                {'id': 'shuzhuangtai',    'name': u'梳妆台/桌',         'children': []},
                {'id': 'shuzhuo',        'name': u'书桌',             'children': []},
                {'id': 'ertongshuzhuo',    'name': u'儿童书桌',         'children': []},
                {'id': 'shuzhuoyizuhe',    'name': u'书桌椅组合',         'children': []},
                {'id': 'diannaozhuo',    'name': u'电脑桌',         'children': []},
                {'id': 'bataibayi',        'name': u'吧台/吧椅',         'children': []},
                {'id': 'majiangzhuo',    'name': u'麻将桌',         'children': []},
            ]},
            {'id': 'jialei',         'name': u'架类',             'children': [
                {'id': 'yimaojia',        'name': u'衣帽架',         'children': []},
                {'id': 'xiejia',        'name': u'鞋架',             'children': []},
                {'id': 'shujia',        'name': u'书架',             'children': []},
                {'id': 'huajia',        'name': u'花架',             'children': []},
                {'id': 'bogujia',        'name': u'博古架',             'children': []},
                {'id': 'gebanbijia',    'name': u'隔板/壁架',         'children': []},
                {'id': 'zazhibaokanjia','name': u'杂志/报刊架',     'children': []},
            ]},
            {'id': 'jilei',         'name': u'几类',             'children': [
                {'id': 'chaji',            'name': u'茶几',             'children': []},
                {'id': 'jiaojibianji',    'name': u'角几/边几',         'children': []},
                {'id': 'taoji',            'name': u'套几',             'children': []},
            ]},
        ]},

    ]
}

keting_tag = {
    'no': '',
    'state': 1,
    'depth': 2,
    'area': 'keting',
    'name': u'客厅',
    'children': [
        {'name': u'沙发', 'children': [
            {'name': u'多人沙发'},
            {'name': u'单人沙发'},
            {'name': u'组合沙发'},
            {'name': u'双人沙发'},
            {'name': u'沙发椅'},
            {'name': u'沙发凳'}
        ]},
        {'name': u'客厅柜类', 'children': [
            {'name': u'电视柜'},
            {'name': u'鞋柜'},
            {'name': u'酒柜'},
            {'name': u'门厅/玄关柜'}
        ]},
        {'name': u'客厅几类', 'children': [
            {'name': u'茶几'},
            {'name': u'角几'},
            {'name': u'套几'}
        ]},
        {'name': u'客厅架类', 'children': [
            {'name': u'衣架帽'},
            {'name': u'鞋架'},
            {'name': u'花架'},
            {'name': u'笔架'},
            {'name': u'杂志/报刊架'}
        ]}
    ]
}

canting_tag = {
    'no': '',
    'state': 1,
    'depth': 2,
    'area': 'canting',
    'name': u'餐厅',
    'children': [
        {'name': u'餐桌椅', 'children': [
            {'name': u'餐桌'},
            {'name': u'餐椅'},
            {'name': u'餐桌椅组合'},

        ]},
        {'name': u'餐厅柜类', 'children': [
            {'name': u'餐边柜'},
            {'name': u'酒柜'},
        ]},
        {'name': u'其他', 'children': [
            {'name': u'餐具'},
            {'name': u'吧椅'},
        ]},

    ]
}

woshi_tag = {
    'no': '',
    'state': 1,
    'depth': 2,
    'area': 'woshi',
    'name': u'卧室',
    'children': [
        {'name': u'床类', 'children': [
            {'name': u'床'},
            {'name': u'单人床'},
            {'name': u'双人床'},

        ]},
        {'name': u'卧室柜类', 'children': [
            {'name': u'柜门'},
            {'name': u'床头柜'},
            {'name': u'衣柜'},
            {'name': u'电视柜'},
            {'name': u'交柜'},
        ]},
        {'name': u'其他', 'children': [
            {'name': u'窗帘'},
            {'name': u'地毯'},
            {'name': u'梳妆台'},
        ]},

    ]
}

shufang_tag = {
    'no': '',
    'state': 1,
    'depth': 2,
    'area': 'shufang',
    'name': u'书房',
    'children': [
        {'name': u'书桌椅', 'children': [
            {'name': u'书桌'},
            {'name': u'写字椅'},
            {'name': u'电脑桌'},
            {'name': u'电脑桌组合'},
            {'name': u'躺椅'}

        ]},

        {'name': u'其他', 'children': [
            {'name': u'书架'},
            {'name': u'书柜'},
            {'name': u'电脑'},
        ]},

    ]
}

ertongfang_tag = {
    'no': '',
    'state': 1,
    'depth': 2,
    'area': 'ertongfang',
    'name': u'儿童房',
    'children': [
        {'name': u'儿童房', 'children': [
            {'name': u'儿童床'},
            {'name': u'高低/母子床'},
            {'name': u'儿童衣柜'},
            {'name': u'儿童书桌'},
            {'name': u'儿童玩具'},
            {'name': u'儿童沙发'},
            {'name': u'婴儿床'}
        ]},
    ]
}

noes = ['a312ff2b9b5946fc839437043e377702', 'f65c05b446004f93a6c162b13c2e5a71', '76dfd87e7d4849d3b41bfac8d6175a9a',
        '7d0774102352493c94511bad29eb2572', '29559980efce4f7a88fa80afe5a0b675', '8e56ad89c07e4cf2af959bf88f828a6b',
        '8e56ad89c07e4cf2af959bf88f828a6b', '6c992da5a7554beba21e47b60da218e0', '8bdb389e3af3423ba4ae81ccfa54927d',
        '7574825e90684b36b456d85b131f9cf8', 'b7634e4938bb4e708db4b0c5d7785c94', 'd93253e4e9244a9f84d86c82d007ea55',
        'f2f467a97f5f4f72b7222e53a9e0dd0a', '3749b1f98f594bcb86b1109cd4ff7435', 'bb2745f56a974eecab75574906124372',
        '1f295b0ba7cc4511b95f2261262a2e2c', '68ed671b9ac445279bf2762863484f59', 'b9b1a60cc86d4dbea264ba0a91343277',
        'c50170b843d54f7cae3abef464a2ad04', 'e2b71a1d8f80460593229c4a022c69b8']

item = {
    "length": 108,
    "top_url": "http://1jbest-3d-img.img-cn-hangzhou.aliyuncs.com/ifuwo/item/15ebce643ad511e7b25300163e0026b6/top.png",
    "cargo_no": "中式风格吊灯DS20170517",
    "sku_id": "",
    "render_state": 3,
    "describe": "",
    "discount_price": 0,
    "system_type": 0,
    "direct_scalable": 1,
    "unit": 1,
    "merchant": ['ifuwo', '1jbest', 'longfa'],
    "user_id": 939,
    "no": "15ebce643ad511e7b25300163e0026b6",
    "product_length": 58.4202805,
    "salable": 0,
    "state": 0,
    "sub_type": 106,
    "product_price": 0,
    "width": 108,
    "product_name": "NO.7652中式风格吊灯DS20170517",
    "status": 40,
    "material": "",
    "scalable": 1,
    "lightable": 1,
    "product_brand": "非商品模型",
    "photo_degree": 45,
    "is_public": 1,
    "sale_count": 0,
    "inner_type": 1,
    "product_id": "",
    "customizable": 0,
    "product_width": 58.4202766,
    "product_link": "",
    "preview_url": "http://1jbest-3d-img.img-cn-hangzhou.aliyuncs.com/ifuwo/1705/17/419073763adf11e7879200163e0026b6.jpg",
    "height": 98,
    "flat_height": 98.3741455,
    "product_height": 98.3741455,
    "author_id": 1,
    "group_id": "",
    "photo_scale": 1.4,
}

