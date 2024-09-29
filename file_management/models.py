from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/' , null=True , blank=True) 
    file2 = models.FileField(upload_to='documents/' , null=True,blank=True)


    def __str__(self):
        return self.title