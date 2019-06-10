from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator


class Solution(models.Model):
    class Meta:
        ordering = ('title',)

    title = models.CharField(unique=True, max_length=200, null=True)
    slug = models.SlugField(unique=True, null=True)
    price = models.DecimalField(max_digits=3, decimal_places=2,
                                validators=[MinValueValidator(0.09)], null=True)
    content = models.TextField(max_length=15000)
    topics = models.ManyToManyField('Topic', related_name='solutions', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Solution, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Topic(models.Model):
    # class Meta:
    #     ordering = ('title',)

    title = models.CharField(unique=True, max_length=200, null=True)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(max_length=2000, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Solution, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

#TODO:
#  remove "blank=True" from topics field in Solution model
