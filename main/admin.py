# from tkinter import Widget
from django.contrib import admin
from .models import Creator, Language, University, Country, UniversityImage, Program, Degree
# Register your models here.





class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name','country','id',)
    prepopulated_fields = {'slug':('name',), 'slug_en':('name_en',),'slug_uz':('name_uz',),'slug_ru':('name_ru',) }


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','image',)
    prepopulated_fields = {'slug':('name',), 'slug_en':('name_en',),'slug_uz':('name_uz',),'slug_ru':('name_ru',) }

class CreatorAdmin(admin.ModelAdmin):
    list_display = ('description','id',)
    list_display_links = ('description','id',)

class UniversityImageAdmin(admin.ModelAdmin):
    list_display = ('university','image', "id")
    list_display_links = ('university','image', "id")



class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name",  "id")


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name",  "id")


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name",  "id")


class RequestAdmin(admin.ModelAdmin):
    list_display = ('university', "name", "id")
    list_display_links = ('university', "name",  "id")



admin.site.register(University, UniversityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(UniversityImage,UniversityImageAdmin )
admin.site.register(Program,ProgramAdmin )
admin.site.register(Language,LanguageAdmin )
admin.site.register(Degree,DegreeAdmin )