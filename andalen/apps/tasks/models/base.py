from django.db import models
#from django.utils.translation import ugettext as _


class Task(models.Model):
	"""
	A Task model
	"""
	name = models.CharField('name', max_length=255)
	date_created = models.DateTimeField('name', auto_now_add=True)
	date_modified = models.DateTimeField('name', auto_now=True) 
	completed = models.BooleanField(default=False)