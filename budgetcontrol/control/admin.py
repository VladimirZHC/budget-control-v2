from django.contrib import admin
from .models import HistoryOperation, Operation, Tag


admin.site.register(Operation)
admin.site.register(Tag)
admin.site.register(HistoryOperation)