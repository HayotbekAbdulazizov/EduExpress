from django.db import models
from django.forms import DateTimeField, ImageField, SlugField
from django.urls import reverse
# from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext as _
from django.utils.translation import get_language
# from parler.models import TranslatableModel, TranslatedFields



# Country Model  ++ University
class Country(models.Model):
    name=models.CharField("Name", max_length=200)
    slug=models.SlugField("Slug")
    image = models.ImageField('Image', upload_to='country_images/', blank=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}"





# University Model  -- Country   ++UniversityImages
class University(models.Model):
    country = models.ForeignKey(Country, null=True, related_name='universities',blank=True, on_delete=models.PROTECT)
    name=models.CharField("Name", max_length=200)
    slug=models.SlugField("Slug")
    rating = models.CharField('Rating', max_length=100, blank=True)
    world_rating = models.CharField('World Rating', max_length=100, blank=True)
    location = models.CharField('Location', max_length=200, blank=True)
    faculties = models.TextField('Faculties', blank=True)
    grands = models.TextField('Grands', blank=True)
    image = models.ImageField('Image', upload_to='university_images/', blank=True)
    description=models.TextField()

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return f"{self.name}"


    def get_absolute_url(self):
        return reverse("main:university_detail", kwargs={"slug": self.slug})


    

# Product TRModel --University ++None
class UniversityImage(models.Model):
    university = models.ForeignKey(University, related_name="images", null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField('University image', upload_to='university_images/')
    class Meta:
        verbose_name = "UniversityImage"
        verbose_name_plural = "UniversityImages"

    def __str__(self):
        return f"{self.university.name}"
    

# Product Model --None ++Request
class Program(models.Model):
    name = models.CharField('Name', max_length=200)
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __str__(self):
        return f"{self.name}"


# Languages TRModel --None ++Request
class Language(models.Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Degree(models.Model):
    name = models.CharField('Name', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Degree"    
        verbose_name_plural = "Degrees"    



# Request Model --Languages,Program,University  ++ None
class Request(models.Model):
    university = models.ForeignKey(University, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField('Name', max_length=200)
    surname = models.CharField("Surname", max_length=200, blank=True)    
    age = models.CharField('Age', max_length=10)
    country = models.CharField('Country', max_length=300, blank=True)
    program = models.ForeignKey(Program, related_name="requests", null=True, blank=True, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, related_name="requests", null=True, blank=True, on_delete=models.PROTECT)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT, blank=True, null=True)
    score = models.FloatField('Score', blank=True, null=True,default=0 )
    phone = models.CharField('Phone Number', max_length=30)

    additional = models.TextField('Message', blank=True)
    date = models.DateTimeField('Date', auto_now_add=True, blank=True)  
    
    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"

    def __str__(self):
        return self.name








# Student class -- University,Language,Program,Request,Country
class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.PROTECT, null=True, blank=True)
    request = models.ForeignKey(Request, on_delete=models.PROTECT, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField('Name', max_length=200, blank=True),
    image = models.ImageField('Student image', upload_to='student_images/'),

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"    
        verbose_name_plural = "Students"    







class Post(models.Model):
    title = models.CharField('Title', max_length=400, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)
    image = models.ImageField('Image Cover', upload_to='news_images/', blank=True)
    description = models.TextField('News description', blank=True)
    date = models.DateTimeField('date', auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"    
        verbose_name_plural = "Posts"    


# PostImage TRModel --Post ++None
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="post_images", null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField('Post image', upload_to='post_images/', blank=True, null=True)
    class Meta:
        verbose_name = "PostImage"
        verbose_name_plural = "PostImages"

    def __str__(self):
        return f"{self.post.title}"