from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = RichTextField(verbose_name="Содержание")
    anons = models.CharField(max_length=200, verbose_name="Анонс", default="")
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
