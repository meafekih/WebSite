from django.db import models

class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(null=True)

