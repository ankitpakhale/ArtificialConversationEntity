from django.db import models

class SignUp(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField(default='')
    age = models.PositiveIntegerField(default=None)
    password = models.CharField(default='', max_length=15)
    confirmPassword = models.CharField(default='', max_length=15)
    def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    phone = models.PositiveIntegerField(default='')
    subject = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=1000, default='')
    def __str__(self):
        return self.name
