from django.db import models

class Card(models.Model):
    numbers = models.IntegerField()
    name = models.CharField(max_length=100)
    subtypes = models.CharField(max_length=500)
    rules = models.CharField(max_length=5000)
    attack_names = models.CharField(max_length=500)

    class Meta:
        db_table = 'output_tbl'
