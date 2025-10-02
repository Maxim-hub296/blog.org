from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = RichTextField(verbose_name="Содержание")
    anons = models.CharField(max_length=200, verbose_name="Анонс", default="")
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class Excerpts(models.Model):
    content = models.TextField()
    background_text = models.TextField()

    def __str__(self):
        return self.content
