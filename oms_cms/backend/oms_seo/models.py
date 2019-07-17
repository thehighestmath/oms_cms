from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Seo(models.Model):
    """SEO модуль"""
    title_page = models.CharField("Title", max_length=60)
    description_page = models.CharField("Description", max_length=150)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.title_page

    class Meta:
        verbose_name = "SEO модуль"
        verbose_name_plural = "SEO модуль"