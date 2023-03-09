from django.db import models

from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=150, verbose_name="Menu title")
    slug = models.SlugField(max_length=50, verbose_name="Slug")

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    slug = models.SlugField(max_length=50, verbose_name="Slug")
    menu = models.ForeignKey(
                            Menu,
                            on_delete=models.CASCADE,
                            blank=False,
                            related_name="items",
                            verbose_name="Menu"
                            )
    parrent = models.ForeignKey(
                            'self',
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE,
                            related_name="childs",
                            verbose_name="Parrent item"
                        )
    nesting_level = models.PositiveIntegerField(
                        default=1, verbose_name="Nesting level"
                        )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('menu_detail', args=[self.menu.slug, self.slug])
    
    class Meta:
        ordering = ["parrent_id"]
