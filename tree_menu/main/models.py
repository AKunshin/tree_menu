from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    slug = models.SlugField(max_length=50, verbose_name="Slug")

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('menu_detail', kwargs={"slug": self.slug})


class Item(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    slug = models.SlugField(max_length=50, verbose_name="Slug")
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name="Menu"
        )

    def get_absolute_url(self):
        return reverse('item', kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title
