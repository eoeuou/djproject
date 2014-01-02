from django.db import models
from django.contrib import admin
# Create your models here.
class QueType(models.Model):
      typeTitle = models.CharField(max_length=200)
      typeDescription = models.TextField()

      def __str__(self):
          return "%s" % (self.typeTitle)

class QueTypeAdmin(admin.ModelAdmin):
      list_display=('typeTitle','typeDescription')

admin.site.register(QueType,QueTypeAdmin)

class Question(models.Model):
      queType = models.ForeignKey(QueType)
      queText = models.CharField(max_length=250)
      ansA = models.CharField(max_length=150)
      ansB = models.CharField(max_length=150)
      ansC = models.CharField(max_length=150)
      ansD = models.CharField(max_length=150)
      rightAns = models.CharField(max_length=100)
      AnsDescription = models.TextField()

class QuestionAdmin(admin.ModelAdmin):
      list_display=('id','queText','ansA','ansB','ansC','ansD','rightAns')

admin.site.register(Question,QuestionAdmin)

