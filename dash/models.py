
from django.db import models

class Profile(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='pictures/', verbose_name="image")
    title1 = models.CharField(max_length=600)
    #contact
    phone = models.CharField(max_length = 20)
    email = models.EmailField()
    address = models.CharField(max_length = 150)
    #about
    bio = models.TextField()
    #social media
    twitter_url = models.URLField()
    facebook_url = models.URLField()
    linkedin_url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.firstname+" - "+self.lastname+" - "+self.image.url

class Education_and_Experience(models.Model):
    organisation = models.CharField(max_length = 200)
    title = models.CharField(max_length = 100)
    summary = models.CharField(max_length = 500)

    def __str__(self):
        return self.organisation+" - "+self.title

class Project(models.Model):
    name = models.CharField(max_length = 201)
    image = models.ImageField(upload_to='pictures/', verbose_name="image")
    project_url = models.URLField(max_length = 100)
    github_url = models.URLField(max_length = 500)

    def __str__(self):
        return self.name
