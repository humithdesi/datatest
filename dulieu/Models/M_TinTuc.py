from django.db import models

class TinTuc(models.Model):
    title=models.CharField(max_length=200,blank=False) 
    content=models.TextField()
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.title