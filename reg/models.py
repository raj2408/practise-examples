from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=42, unique=True)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    institute = models.ForeignKey('Institute', on_delete=models.PROTECT, blank=True, null=True,)
    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    subject = models.CharField(max_length=20)
    institute = models.ManyToManyField('Institute')
    def __str__(self):
        return self.name




class Institute(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name