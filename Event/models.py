from django.db import models

# Create your models here.
class Email(models.Model):
    name =  models.CharField(max_length=122)
    roll = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.TextField()
    date = models.DateField()
    toMail = models.EmailField()
    fromMail = models.EmailField()
    submittedOn = models.DateTimeField(auto_now_add=True,null=True)

class Timings(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Timings'