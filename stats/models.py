from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Statistic(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"), blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("stats:dashboard", kwargs={"slug": self.slug})
    
    @property
    def data(self):
        return self.statistic_dataitems.all()

    def __str__(self):
        return self.name



class DataItem(models.Model):
    statstic = models.ForeignKey(Statistic, related_name='statistic_dataitems', verbose_name=_("Statistic"), on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(_("Value"))
    user = models.CharField(_("User"), max_length=50)

    def __str__(self):
        return f"{self.user} - {self.value}"