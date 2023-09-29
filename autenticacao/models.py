from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Usuário', unique=True)
    email = models.EmailField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        else:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)