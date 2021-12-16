from django.db import models

# Create your models here.
class HocSinh(models.Model):
    name=models.CharField(max_length=50,blank=False)
    age=models.IntegerField()
    description=models.TextField()
    def __str__(self):
        return self.name