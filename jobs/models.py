from django.db import models
from django.contrib import admin

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        if self.state:
            return "%s, %s, %s" % (self.city, self.state, self.country)
        else:
            return "%s, %s" % (self.city, self.country)
    
    def toJson(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Job(models.Model):
    pub_date = models.DateField()
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    location = models.ForeignKey(Location)

    def __str__(self):
        return "%s (%s)" % (self.job_title, self.location)
    def toJson(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

admin.site.register(Location)

class JobAdmin(admin.ModelAdmin):
    #fields = ['pub_date','job_title','job_description','location']
    fieldsets = [(None,{'fields':['pub_date']}),('INFO',{'fields':['job_title','job_description','location']})]
admin.site.register(Job,JobAdmin)

