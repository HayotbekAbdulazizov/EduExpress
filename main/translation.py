from modeltranslation.translator import translator, TranslationOptions
from .models import Country, University, UniversityImage, Program, Language, Degree, Request, Student, Post, PostImage


class UniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'slug','rating','world_rating','location','faculties','grands','description','image' )



class CountryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug','image' )



class UniversityImageTranslationOptions(TranslationOptions):
    fields = ('university', 'image' )



class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', )



class LanguageTranslationOptions(TranslationOptions):
    fields = ('name', )



class DegreeTranslationOptions(TranslationOptions):
    fields = ('name', )



# class RequestTranslationOptions(TranslationOptions):
    # fields = ('university', 'name','surname','age','country','program','language','degree','score','phone','additional',  )



# class StudentTranslationOptions(TranslationOptions):
    # fields = ('name', 'slug','rating','world_rating','location','faculties','grands','description','image' )


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug','image','description','date' )


class PostImageTranslationOptions(TranslationOptions):
    fields = ('post', 'image')










translator.register(University , UniversityTranslationOptions)
translator.register(Country , CountryTranslationOptions)
translator.register(UniversityImage , UniversityImageTranslationOptions)
translator.register(Program, ProgramTranslationOptions)
translator.register(Language , LanguageTranslationOptions)
translator.register(Degree, DegreeTranslationOptions)
translator.register(PostImage, PostImageTranslationOptions)
translator.register(Post , PostTranslationOptions)
