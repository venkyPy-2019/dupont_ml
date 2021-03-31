from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django_countries.fields import CountryField
from django.utils.timezone import now

# Create your models here.
class researchUpdate(models.Model):
	blog_title = models.CharField(max_length=225)
	blog_desc = HTMLField()
	blog_date = models.DateField()
	blog_image = models.ImageField(upload_to='media/blog_img')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=now, editable=False)
	def __str__(self):
		return self.blog_title

class MachineLearningModelReference(models.Model):
	title = models.CharField(max_length=225)
	description = HTMLField()
	image = models.ImageField(upload_to='media/references')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=now, editable=False)
	def __str__(self):
		return self.title

class Contact(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	company_name = models.CharField(max_length=225)
	email_address = models.EmailField()
	country = CountryField(blank_label='--Select Country--')
	phone_no = models.IntegerField()
	CHOICES=[('email','Email'),
         	('phone','Phone')]
	contact_prefer = models.CharField(choices=CHOICES, max_length=65, default='email')
	question = models.TextField()
	receive_alerts = models.BooleanField(default='0')
	created_at = models.DateTimeField(default=now, editable=False)
	def __str__(self):
		return self.first_name

class ImagePred(models.Model):
	image = models.ImageField(upload_to='media/image_pred')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=now, editable=False)
	def __str__(self):
		return self.created_by
