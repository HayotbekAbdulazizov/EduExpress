from modeltranslation.translator import translator, TranslationOptions
from .models import Country, Creator, University, Program, Language, Degree, Student, Post, ClientRequest


class UniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'slug','rating','world_rating','location','description','image' )



class CountryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')



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



class CreatorTranslationOptions(TranslationOptions):
    fields = ('description',)








translator.register(University , UniversityTranslationOptions)
translator.register(Country , CountryTranslationOptions)
translator.register(Program, ProgramTranslationOptions)
translator.register(Language , LanguageTranslationOptions)
translator.register(Degree, DegreeTranslationOptions)
translator.register(Post , PostTranslationOptions)
translator.register(Creator , CreatorTranslationOptions)
