from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/' , null=True)
    file2 = models.FileField(upload_to='documents/' , null=True)


    def __str__(self):
        return self.description