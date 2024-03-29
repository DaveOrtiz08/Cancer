from django.db import models

# Create your models here.
class Pacientes(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Paciente")
        verbose_name_plural = ("Pacientes")

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("Paciente_detail", kwargs={"pk": self.pk})

''
class Tessiu(models.Model):
    temperatura = models.FloatField()
    color = models.FloatField()
    inflammation= models.FloatField(verbose_name="Inflamacion")
    name = models.ForeignKey(Pacientes, blank=True, null=True, verbose_name="nombre", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Tejido")
        verbose_name_plural = ("Tejidos")

    def __str__(self):
        if self.name is not None:
            return str(self.temperatura)
        else:
            return str(self.temperatura)

    def get_absolute_url(self):
        return reverse("Tejido_detail", kwargs={"pk": self.pk})


