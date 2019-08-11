from django.contrib import admin
from shortener.models import Url
# Register your models here.


# Register your models here.
class UrlAdmin(admin.ModelAdmin):
    list_display=['main_url','new_url']

admin.site.register(Url,UrlAdmin)

# Register your models here.
