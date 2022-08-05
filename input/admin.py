from django.contrib import admin
from .models import Input


class InputAdmin(admin.ModelAdmin):
    pass
admin.site.register(Input, InputAdmin)