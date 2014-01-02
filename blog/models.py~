from django.db import models
from django.contrib import admin
# Create your models here.
class BlogPost(models.Model):
      title = models.CharField(max_length=150)
      body = models.TextField()
      timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
      list_display=('title','timestamp')

admin.site.register(BlogPost,BlogPostAdmin)

class Author(models.Model):
      name = models.CharField(max_length=100)    
      def __str__(self):
            return "%s,%s" % (self.id, self.name)

class AuthorAdmin(admin.ModelAdmin):
      list_display=('id','name')

admin.site.register(Author,AuthorAdmin)

class Book(models.Model):
      title = models.CharField(max_length=150)
      author = models.ForeignKey(Author)
      length = models.IntegerField()

class BookAdmin(admin.ModelAdmin):
      list_display=('title','length')

admin.site.register(Book,BookAdmin)
