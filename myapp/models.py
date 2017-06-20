# from django.db import models

# # Create your models here.

# class RegistrationForm(models.Model):
# 	first_name = models.CharField(max_length=45)
# 	last_name = models.CharField(max_length=45)
# 	email = models.EmailField()
# 	password = models.CharField(max_length=100)#,widget=models.PasswordInput)
# 	confirm_password = models.CharField(max_length=100)#,widget=models.PasswordInput)

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Crop_details(models.Model):
	Name = models.CharField(max_length=30)
	Phone = models.IntegerField()
	FieldLocation = models.CharField(max_length=30)
	CropAcres = models.IntegerField()