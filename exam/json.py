#!/usr/bin/env python 
#coding=utf-8
# Create your views here.
import urllib
import re

from django.utils import simplejson
from django.db import models
from django.core.serializers import serialize,deserialize
from django.db.models.query import QuerySet

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

#======================json=======================

#====================json model===============================

#def jobs_list(request):
    #jdata = getJson(Job.objects.all())
    #return HttpResponse(jdata)

#====================json model===============================

