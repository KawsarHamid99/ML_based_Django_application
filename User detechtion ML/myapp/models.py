from django.db import models

# Create your models here.
from django.db import models

class Video(models.Model):
    file = models.FileField(upload_to='videos/')