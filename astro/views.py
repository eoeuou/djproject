#!/usr/bin/env python 
#coding=utf-8
# Create your views here.
import urllib
import re
import datetime
import sqlite3

from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404, HttpResponse
from django.utils import simplejson
from django.db import models
from django.core.serializers import serialize,deserialize
from django.db.models.query import QuerySet

from astro.models import AstroModel,AstroModelAdmin
from astro.json import getJson

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()#.decode('gbk')
    page.close()
    return html

def getResults(html,reg):
    astroList=re.compile(reg).findall(html)
    return astroList

def getAstro_name(html):
    regName = '<span>(.*?)<em>(.*?)</em></span>'
    result = {'title':'星座','value':getResults(html,regName)} 
    return result

def getAstro_conts(html):
    regContent = '<div class="lotconts">(.*?)</div>'
    result = {'title':'内容','value':getResults(html,regContent)}
    return result

def getAstro_day(html):
    regContent = '<li class="buton">(.*?)</li>'
    print getResults(html,regContent)
    result = {'title':getResults(html,regContent)}
    print result
    return result

def getAstro_others(html):
    regContent='<div class="tab"><h4>(.*?)</h4><p>(.*?)</p></div>'
    return getResults(html,regContent)

def getAstro_json(html):
    res = []
    res.append(getAstro_day(html))
    res.append(getAstro_name(html))
    res.append(getAstro_conts(html))
    results = getAstro_others(html)
    for element in results:
        if cmp(element[0],"&nbsp;")==0:
           continue
        result = {}
        result['title'] = element[0]
        result['value'] = element[1]
        res.append(result)
    
    return res

def getCpp_json(html):
    #regContent='<h1 class="artTitle size_16 col_666">(.*?)</h1>'
    regContent='<div id="article" class="over_hidden">(.*?)</div>'
    return getResults(html,regContent)

def getCpp(request):
    html = getHtml('http://see.xidian.edu.cn/cpp/biancheng/view/103.html')
    print html
    return HttpResponse(simplejson.dumps(getCpp_json(html),ensure_ascii=False))

def astro(request):
    html = getHtml('http://vip.astro.sina.com.cn/astro/view/taurus/day/')
    #return HttpResponse(getAstro_json(html))
    return HttpResponse(simplejson.dumps(getAstro_json(html),ensure_ascii=False))

def astro_id(request, offset):
    if(offset>11):
        offset = int(offset) % 12
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    astro_arr = [
    "http://vip.astro.sina.com.cn/iframe/astro/view/aries/day/", #白羊座
    "http://vip.astro.sina.com.cn/iframe/astro/view/taurus/day/", #金牛座
    "http://vip.astro.sina.com.cn/iframe/astro/view/gemini/day/", #双子座
    "http://vip.astro.sina.com.cn/iframe/astro/view/cancer/day/", #巨蟹座
    "http://vip.astro.sina.com.cn/iframe/astro/view/leo/day/", #狮子座
    "http://vip.astro.sina.com.cn/iframe/astro/view/virgo/day/", #处女座
    "http://vip.astro.sina.com.cn/iframe/astro/view/libra/day/", #天秤座
    "http://vip.astro.sina.com.cn/iframe/astro/view/scorpio/day/", #天蝎座
    "http://vip.astro.sina.com.cn/iframe/astro/view/sagittarius/day/", #射手座
    "http://vip.astro.sina.com.cn/iframe/astro/view/capricorn/day/", #魔羯座
    "http://vip.astro.sina.com.cn/iframe/astro/view/aquarius/day/", #水瓶座
    "http://vip.astro.sina.com.cn/iframe/astro/view/pisces/day/", #双鱼座
    ]

    json = getAstro_json(getHtml(astro_arr[offset]))
    return HttpResponse(simplejson.dumps(json,ensure_ascii=False))

def get_astro(request):
    id = request.GET.get('id')
    if id==None or int(id)<=0:
       id = 1
    sql_insert()
    return astro_id(request,id)

def sql_insert():
    cx=sqlite3.connect("database_2.db")
    #cx.execute("delete from astro_astromodel")
    cur = cx.cursor()
    cur.execute("select * from astro_astromodel")
    res = cur.fetchall()
    print len(res)
    cx.execute("insert into astro_astromodel values (?,'xx','xx','2','xx')",(len(res)+1,))
    cx.commit()
    cx.close()
