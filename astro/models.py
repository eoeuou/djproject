from django.db import models
from django.contrib import admin
# Create your models here.
class AstroModel(models.Model):
      astroName = models.CharField(max_length=50)
      astroData = models.CharField(max_length=50)
      astroConts = models.CharField(max_length=200)
      today = models.CharField(max_length=50)

      def __str__(self):
          return "%s" % (self.astroName,today)

class AstroModelAdmin(admin.ModelAdmin):
      list_display=('astroName','today')

admin.site.register(AstroModel,AstroModelAdmin)

