from django.contrib import admin
from .models import Operation, Tag


admin.site.register(Operation)
admin.site.register(Tag)