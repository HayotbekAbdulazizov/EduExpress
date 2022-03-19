from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext as _
from django.utils.translation import get_language
from parler.models import TranslatableModel, TranslatedFields
from parler.utils.context import switch_language



# Country Model  ++ University
class Country(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField("Name", max_length=200),
        slug=models.SlugField("Slug"),
        image = models.ImageField('Image', upload_to='country_images/', blank=True),
        # meta={"unique_together": (("slug", "language_code"),),},
    )

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}"





# University Model  -- Country   ++UniversityImages
class University(TranslatableModel):

    country = models.ForeignKey("Country", null=True, related_name='universities',blank=True, on_delete=models.PROTECT)
    translations = TranslatedFields(
        name=models.CharField("Name", max_length=200),
        slug=models.SlugField("Slug"),
        rating = models.CharField('Rating', max_length=100, blank=True),
        world_rating = models.CharField('World Rating', max_length=100, blank=True),
        location = models.CharField('Location', max_length=200, blank=True),
        faculties = models.TextField('Faculties', blank=True),
        grands = models.TextField('Grands', blank=True),
        image = models.ImageField('Image', upload_to='university_images/', blank=True),
        description=models.TextField(),
        meta={"unique_together": (("slug", "language_code"),),},
    )

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return f"{self.name}"


    def get_absolute_url(self):
        with switch_language(self):
            return reverse("main:university_detail", kwargs={"slug": self.slug})

    def get_all_slugs(self):
        return dict(self.translations.values_list("language_code", "slug"))

    

# Product Images
class UniversityImage(TranslatableModel):
    university = models.ForeignKey("University", related_name="images", null=True, blank=True, on_delete=models.CASCADE)
    translations = TranslatedFields(
        image = models.ImageField('University image', upload_to='university_images/'),
    )
    class Meta:
        verbose_name = "UniversityImage"
        verbose_name_plural = "UniversityImages"

    def __str__(self):
        return f"{self.university.name}"
    



# Message Model --++ None
class Message(models.Model):
    name = models.CharField(_('Name'), max_length=200, blank=True)
    email = models.EmailField('Email', max_length=300, blank=True)
    phone = models.CharField(_('Phone Number'), max_length=30, blank=True)
    additional = models.TextField(_('Additional Message'), blank=True)
    date = models.DateTimeField(_('Date'), auto_now_add=True, blank=True)
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.name