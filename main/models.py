from django.db import models
class HideURL(models.Model):
    md5sum = models.CharField(max_length=40)
    url = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "redirect anywhere"
# Create your models here.
