from modeltranslation.translator import translator, TranslationOptions
from .models import Country, University, UniversityImage, Program, Language, Degree, Request, Student, Post, PostImage

class UniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'slug','rating','world_rating','location','faculties','grands','description','image' )

translator.register(University , UniversityTranslationOptions)