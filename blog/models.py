from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    #this is to display the blog post titles in the dashboard with the acutal title
    def __str__(self):
        return self.title