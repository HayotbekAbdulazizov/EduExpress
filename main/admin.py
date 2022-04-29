# from tkinter import Widget
from django.contrib import admin
from .models import Creator, Language, Post, University, Country,  Program, Degree, ClientRequest
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


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name",  "id")


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name",  "id")


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', "id")
    list_display_links = ("name",  "id")


class ClientRequestAdmin(admin.ModelAdmin):
    list_display = ('university', "name", "phone","id")
    list_display_links = ('university', "name",  "id")

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  "date", "id")
    list_display_links = ("title", "date","id")
    prepopulated_fields = {'slug':('title',), 'slug_en':('title_en',),'slug_uz':('title_uz',),'slug_ru':('title_ru',) }



admin.site.register(University, UniversityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(Program,ProgramAdmin )
admin.site.register(Language,LanguageAdmin )
admin.site.register(Degree,DegreeAdmin )
admin.site.register(Post,PostAdmin)
admin.site.register(ClientRequest,ClientRequestAdmin)