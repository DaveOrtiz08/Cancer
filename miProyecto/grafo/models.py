from django.db import models

# Create your models here.
class Grafos(models.Model):
    temperatura = models.FloatField()
    
    class Meta:
        verbose_name = ("Grafo")
        verbose_name_plural = ("Grafos")

    def __str__(self):
        if self.name is not None:
            return str(self.temperatura)
        else:
            return str(self.temperatura)

    def get_absolute_url(self):
        return reverse("Grafo_detail", kwargs={"pk": self.pk})
