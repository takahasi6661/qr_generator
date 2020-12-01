from django.db import models

# Create your models here.
class Site(models.Model):
    class Meta:
        db_table='sites'
    name=models.CharField(max_length=150,db_index=True)
    description=models.TextField(blank=True,db_index=True)
    url=models.TextField(blank=True,db_index=True)
    image=models.ImageField()

    def __str__(self):
        return self.name
# class Image(models.Model):
#     class Meta:
#         db_table='image'
#     title = models.CharField(max_length=200)
#     image = models.ImageField()
#
#     def __str__(self):
#         return self.title
