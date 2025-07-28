from django.db import models



class Footer(models.Model):
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    instagram_url = models.CharField(max_length=100)
    whatsapp_url = models.CharField(max_length=100)
    telegram_url = models.CharField(max_length=100)



class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"