from django.contrib import admin

# Register your models here.
from .models import matches, match, school

admin.site.register(matches)
admin.site.register(match)
admin.site.register(school)