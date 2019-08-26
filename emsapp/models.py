from django.db import models

# Create your models here.

class Emplist(models.Model):
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    age = models.SmallIntegerField()
    headpic = models.ImageField(upload_to='pics')

    class Meta:
        db_table = "emplist"