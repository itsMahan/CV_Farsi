from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='projects_images/')


    def __str__(self):
        return self.title
