from django.db import models

# Create your models here.
class pomps(models.Model):
    brand=models.CharField(max_length=70)
    modelnum=models.CharField(max_length=70)
    price=models.IntegerField()
    madein=models.CharField(max_length=70)
    slug=models.SlugField()
    discription=models.TextField(null=True)

    def __str__(self):
        return self.brand

    def snippet(self):
        return self.discription[:50]+ '  ...'
