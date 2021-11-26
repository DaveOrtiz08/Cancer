from django.db import models

# Create your models here.
class Body(models.Model):
    zones = models.CharField(max_length=50, blank=True,null=True)
    porcent = models.FloatField()
    tratamient = models.CharField(max_length=50, blank=True,null=True)


    class Meta:
        verbose_name = ("Cuerpo")
        verbose_name_plural = ("Cuerpos")
    
    def __str__(self):
        if self.name is not None:
            return str(self.zones) + self.tratamient
        else:
            return str(self.zones)

    def get_absolute_url(self):
        return reverse("Cuerpo_detail", kwargs={"pk": self.pk})
