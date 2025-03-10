from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=900)
    content = models.CharField(max_length=10000)
    category = models.CharField(max_length=45)
    imagen = models.ImageField(upload_to='post_images/', null=True, blank=True)

class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    githubaccount = models.CharField(max_length=30)

class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    message = models.CharField(max_length=700)