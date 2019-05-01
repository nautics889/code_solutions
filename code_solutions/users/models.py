from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_superior = models.BooleanField(_('admin status'),
                                      default=False)
    is_redactor = models.BooleanField(_('redactor status'),
                                      default=False)
    #TODO:
    # add field for email verification status

    def __str__(self):
        return f'{self.id}/{self.username}'
