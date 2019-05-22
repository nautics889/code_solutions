from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator


class TitleDescriptionSlugMixin:
    title = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=2000)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)


class Solution(models.Model, TitleDescriptionSlugMixin):
    price = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.09)])

    content = models.TextField(max_length=15000)

    topics = models.ManyToManyField('Topic', related_name='solutions', blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Topic(models.Model, TitleDescriptionSlugMixin):
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return

#TODO:
#  create abstraction beyond Topic and Model
#  remove "blank=True" from topics field in Solution model
