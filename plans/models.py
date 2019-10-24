from django.db import models

# Create your models here.
class Laan(models.Model):
    laanebelop = models.FloatField(default=0)
    nominellRente = models.FloatField(default=0)
    terminGebyr = models.FloatField(default=0)
    utlopsDato = models.DateField()
    saldoDato = models.DateField()
    datoForsteInnbetaling = models.DateField()

    def __str__(self):
        return "Lån" + str(self.id)

class Innbetaling(models.Model):
    laan = models.ForeignKey(Laan, on_delete=models.CASCADE)
    restgjeld = models.FloatField(default=0)
    dato = models.DateField()
    gjeldsbetaling = models.FloatField(default=0)
    gebyr = models.FloatField(default=0)
    renter = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return "Innbetaling" + str(id)
