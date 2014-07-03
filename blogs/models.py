from django.db import models

# Create your models here.

class Blog(models.Model):
    content = models.TextField()
    writer = models.CharField(max_length=50)
    published_at = models.DateTimeField()
    email = models.EmailField()
    title = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    body = models.TextField(max_length=500)
    posted_by = models.EmailField()
    posted_at = models.DateTimeField()