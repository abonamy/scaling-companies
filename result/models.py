from django.db import models


class Company(models.Model):

    class Sector(models.TextChoices):
        ELECTRONIC = 'E', 'Electronic'
        ENERGY = 'N', 'Energy'
        LUXURY = 'L', 'Luxury'
        RETAIL = 'R', 'Retail'
        SERVICES = 'S', 'Services'

    name = models.CharField(max_length=100)
    siren = models.IntegerField(default=0)  # nine digits
    sector = models.CharField(max_length=1, choices=Sector.choices)

    class Meta:
        ordering = ['name']  # !case sensitive (abcABC)
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Result(models.Model):
    ca = models.IntegerField(default=0)
    ebitda = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    margin = models.IntegerField(default=0)
    year = models.SmallIntegerField(default=0)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='results')

    class Meta:
        ordering = ['company', 'year']

    def __str__(self):
        return f"{self.company} - {self.year}"
