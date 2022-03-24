# from tkinter import Widget
from django.contrib import admin
from .models import University, Country
# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name','slug','id',)
    prepopulated_fields = {'slug':('name',), 'slug_en':('name_en',),'slug_uz':('name_uz',),'slug_ru':('name_ru',) }


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','image',)
    prepopulated_fields = {'slug':('name',), 'slug_en':('name_en',),'slug_uz':('name_uz',),'slug_ru':('name_ru',) }

# class UniversityAdmin(admin.ModelAdmin):
    # list_display = ('name','slug','id',)
    # prepopulated_fields = {'slug':('name',), 'slug_en':('name_en',),'slug_uz':('name_uz',),'slug_ru':('name_ru',) }


admin.site.register(University, UniversityAdmin)
admin.site.register(Country, CountryAdmin)

