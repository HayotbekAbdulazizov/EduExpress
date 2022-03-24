# from tkinter import Widget
from django.contrib import admin
from .models import (
    University,
)
# Register your models here.

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name','slug','id',)
    prepopulated_fields = {'slug':('name',), 'slug_en':('name_en',),'slug_uz':('name_uz',),'slug_ru':('name_ru',) }
    # prepopulated_fields = {'slug_en':('name_en',)}
    # prepopulated_fields = {'slug_uz':('name_uz',)}
    # prepopulated_fields = {'slug_ru':('name_ru',)}


# class BlogAdmin(admin.ModelAdmin):
    # list_display = ('title','content','slug',    )



admin.site.register(University, UniversityAdmin)

