from django.contrib import admin
from .models import  HistoryOperation, Operation, Tag, Currency


admin.site.register(Operation)
admin.site.register(Tag)
admin.site.register(HistoryOperation)
admin.site.register(Currency)