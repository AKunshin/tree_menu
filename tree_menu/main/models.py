from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    slug = models.SlugField(max_length=50, verbose_name="Slug")
    parrent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="childs",
        verbose_name="Parrent item"
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('index', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["parrent_id"]
