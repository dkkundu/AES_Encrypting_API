from django.db import models

# Create your models here.


class UserBankInformation(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=100,  null=False, blank=False)
    bank_account = models.CharField(max_length=100, null=False, blank=False)
    photo = models.TextField(null=False, blank=False)
    bank_pin = models.CharField(max_length=10, null=False, blank=False)
    ref = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name