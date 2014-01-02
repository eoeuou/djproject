#!/usr/bin/env python 
#coding=utf-8
import urllib
import re
from django.db import models

class Astro(models.Model):
	def getHtml(url):
	    page=urllib.urlopen(url)
	    html=page.read()
	    page.close()
	    return html

	def getResults(html,reg):
	    astroList=re.compile(reg).findall(html)
	    return astroList

	html = getHtml('http://vip.astro.sina.com.cn/astro/view/taurus/day/')

	def getAstro_name():
	    regName = '<span>(.*?)<em>.*?</em></span>'
	    return getResults(html,regName)

	def getAstro_conts():
	    regContent='<div class="lotconts">(.*?)</div>'
	    return getResults(html,regContent)

