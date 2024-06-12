from django.db import models

# Create your models here.
class Employee(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, default='Unknown')
    state = models.CharField(max_length=255)
    adoption = models.CharField(max_length=255)
    reimbursement = models.CharField(max_length=255)
    csection = models.CharField(max_length=255)

class Messages(models.Model):
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    message = models.TextField()