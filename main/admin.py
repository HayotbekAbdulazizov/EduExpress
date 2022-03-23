# from tkinter import Widget
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget, AdminTextInputWidget
from django.urls import clear_script_prefix
from parler.admin import TranslatableAdmin, TranslatableStackedInline, TranslatableTabularInline
from parler.forms import TranslatableModelForm, TranslatedField
from .models import *



# Stacked ADMINS
class UniversityImageStacked(TranslatableStackedInline):
    model = UniversityImage
    extra = 1

class PostImageStacked(TranslatableStackedInline):
    model = PostImage
    extra = 1



# University Admin
class CountryAdmin(TranslatableAdmin):
    list_display = ("name","id")
    fieldsets = ((None,{"fields": ("name", "slug","image"),},),)

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}



# University Admin
class UniversityAdmin(TranslatableAdmin):
    inlines = [UniversityImageStacked]
    list_display = ("name", "country","id") 
    fieldsets = ((None,{"fields": ("name", "country","slug", "rating", "world_rating", "location", "faculties", "grands", "image", "description"),},),)

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}





class PostAdmin(TranslatableAdmin):
    inlines = [PostImageStacked]
    list_display = ("title","date","id")
    fieldsets = ((None,{"fields": ("title","slug", "image", "description", "date", "id"),},),)

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("title",)}

    




class ProgramAdmin(TranslatableAdmin):
    list_display = ("name","id")
    fieldsets = ((None,{"fields": ("name",),},),)


class LanguageAdmin(TranslatableAdmin):
    list_display = ("name","id")
    fieldsets = ((None,{"fields": ("name",),},),)

class DegreeAdmin(TranslatableAdmin):
    list_display = ("name","id")
    fieldsets = ((None,{"fields": ("name",),},),)

class StudentAdmin(TranslatableAdmin):
    list_display = ("name","university","country")
    fieldsets = ((None,{"fields": ("name","university", "language", "program", "request", "country"),},),)



@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "date"]
    list_display_links = ["name", "phone", "date"]




admin.site.register(Country, CountryAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Degree,DegreeAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(UniversityImage)
admin.site.register(PostImage)



