from django.db import models
import uuid 


def uploadImageFormater(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"

class Contact(models.Model):
    foto = models.ImageField(upload_to=uploadImageFormater, null=True, blank=True)
    name = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
