from django.db import models

# Create your models here.
#inheritted from django.db.models.Model
class Blog(models.Model):
	content = models.TextField()
