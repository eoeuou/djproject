# Create your views here.
from django.template import loader,Context
from django.http import Http404, HttpResponse
from django.db import models
from django.db.models.query import QuerySet

from exam.models import QueType,Question
from exam.json import getJson

def get_types(request):
    types = QueType.objects.all()
    json = getJson(types)
    html = 'types:<br>'
    for typeid in types:
       html += typeid.typeTitle+"<br>"
    return HttpResponse(json)

def get_qeustions(request):
    page = request.GET.get('p')
    if page==None or int(page)<=0:
       page = 1
    quetype = request.GET.get('type')
    if quetype==None:
       quetype = 1
    num = request.GET.get('num')
    if num==None:
       num = 2
    begin = num*(int(page)-1)
    end = num*int(page)
    questions = Question.objects.filter(queType_id=quetype)[begin:end]
    return HttpResponse(getJson(questions))
    


