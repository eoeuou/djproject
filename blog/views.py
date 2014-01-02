import datetime
from django.template import loader,Context
from django.http import HttpResponse
from django.db.models.query import QuerySet

from blog.models import BlogPost,Book

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'blogs':posts})
    return HttpResponse(t.render(c))

def get_now(request):
    now = datetime.datetime.now()
    return HttpResponse('now:%s'%now)

def get_books(request):
    books = Book.objects.all()
    html = 'books:<br>'
    for book in books:
       html += book.title+"<br>"
       print book.title     
    return HttpResponse(html)
