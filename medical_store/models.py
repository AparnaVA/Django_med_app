from django.db import models

class medicine(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
