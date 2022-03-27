from django.contrib import admin
from hello_world.models import AccessRecord, Topic, WebPage
# Register your models here.

admin.site.register([AccessRecord, Topic, WebPage])
