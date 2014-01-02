#!/usr/bin/env python 
#coding=utf-8
# Create your views here.
import urllib
import re
import datetime

from django.template import Context, loader
from django.http import HttpResponse
from django.http import Http404, HttpResponse
from django.utils import simplejson
from django.db import models
from django.core.serializers import serialize,deserialize
from django.db.models.query import QuerySet

from jobs.models import Job
from jobs.models import Location
#======================json=======================
class MyEncoder(simplejson.JSONEncoder):
    def default(self,obj):
            if isinstance(obj,QuerySet):
                return simplejson.loads(serialize('json',obj))
            if isinstance(obj,models.Model):
                return simplejson.loads(serialize('json',[obj])[1:-1])
            if hasattr(obj, 'isoformat'):
                return obj.isoformat()
            return simplejson.JSONEncoder.default(self,obj)

def jsonBack(json):
    if json[0] == '[':
        return deserialize('json',json)
    else:
        return deserialize('json','[' + json +']')

def getJson(result):
    return simplejson.dumps(result,cls=MyEncoder)

#def hello(request):
    #return HttpResponse("Hello World")
#======================json=======================
#======================星座=======================

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

#======================星座=======================
#=======================json test============================

def index(request):
    object_list = Job.objects.order_by('-pub_date')[:10]
    t = loader.get_template('job_list.html')
    c = Context({
	'object_list':object_list,
    })
    return HttpResponse(t.render(c))

def get_host_json(request):
    json = {'name':'jiang'}
    return HttpResponse(simplejson.dumps(json, ensure_ascii=False))

def some_view(request):
    to_json = {
        "key1": "value1",
        "key2": "value2"
    }
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

#====================json model===============================

from django.core import serializers
def jobs_list(request):
    #object_list = Location.objects.all()
    #jsonstr = json_encode(object_list)
    #raw = Location.objects.get(id=1)
    #print raw.toJson()
    
    #data = serializers.serialize("json", Location.objects.all())
    #print data
    #print jsonBack(jdata)
    #data = serializers.serialize('xml', Location.objects.all())
    #return HttpResponse(simplejson.dumps(jsonstr), mimetype='application/json')
    #return HttpResponse(simplejson.dumps(raw.toJson()), mimetype='application/json')
    #return HttpResponse(simplejson.dumps(data, ensure_ascii=False),mimetype='application/json')
    jdata = getJson(Job.objects.all())
    print jdata
    return HttpResponse(jdata)

#=======================datetime===============================

def current_datetime(request):
    now = datetime.datetime.now() 
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

# plus_or_minus和offset参数由urls.py中设置，这里的设置是  
#(r'^now/(plus|minus)(\d{1,2})hours/$', hello.hours_offset),  
#与位置顺序有关  
def hours_offset(request,plus_or_minus,offset):  
    offset=int(offset)  
    print offset
    if plus_or_minus=='plus':  
        dt=datetime.datetime.now()+datetime.timedelta(hours=offset)  
        html="In %s hour(s) ,it will be %s." %(offset,dt);  
    else:  
         dt=datetime.datetime.now()-datetime.timedelta(hours=offset)  
         html="%s hour(s) ago,it will be %s." %(offset,dt)  
    return HttpResponse(html)  
