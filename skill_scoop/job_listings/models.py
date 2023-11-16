from django.db import models
# from user_management.models import Skill

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title
