from django.db import models

# Create your models here.
class Intern(models.Model):
    namePa = models.CharField(max_length=50, blank=True,null=True)
    age = models.FloatField()
    date = models.CharField(max_length=50, blank=True,null=True)

    class Meta:
        verbose_name = ("Interno")
        verbose_name_plural = ("Internos")

    def __str__(self):
        if self.name is not None:
            return str(self.namePa) + self.date
        else:
            return str(self.namePa)

    def get_absolute_url(self):
        return reverse("Interno_detail", kwargs={"pk": self.pk})

