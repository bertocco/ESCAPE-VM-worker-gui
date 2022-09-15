from django.db import models

# Create your models here.

class CreateVM(models.Model):
    vm_name_value = models.CharField(max_length=255, blank=True, null=True)
    token_value = models.CharField(max_length=3000, blank=True, null=True)
    ssh_key_value = models.CharField(max_length=25, blank=True, null=True)

