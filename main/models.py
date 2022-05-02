from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="doclist")
    docName = models.CharField(max_length=25)
    docFile = models.FileField(upload_to="media")

    def __str__(self):
        return self.docName