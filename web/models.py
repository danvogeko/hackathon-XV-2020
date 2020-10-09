from django.db import models

# Create your models here.
class change(models.Model):
	text=models.CharField(max_length=200)

	def __str__(self):
		return self.text


	#1 - Background color
	#2 - Text

class text(models.Model):
	text=models.CharField(max_length=255)

	def __str__(self):
		return self.text