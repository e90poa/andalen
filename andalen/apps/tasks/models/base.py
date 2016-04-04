from django.db import models
#from django.utils.translation import ugettext as _


class Tag(models.Model):
	"""
	A Tag
	"""
	name = models.CharField('name', max_length=255)

	class Meta:
		app_label = 'tasks'



class TagTask(models.Model):
	"""
	A Tag Task
	"""
	tag = models.ForeignKey('Tag', verbose_name='tag')
	task = models.ForeignKey('Task', verbose_name='task')

	class Meta:
		app_label = 'tasks'

class Folder(models.Model):
	"""
	A Folder
	"""
	name = models.CharField('name', max_length=255)

	class Meta:
		app_label = 'tasks'



class Task(models.Model):
	"""
	A Task model
	"""
	name = models.CharField('name', max_length=255)
	date_created = models.DateTimeField('date created', auto_now_add=True)
	date_modified = models.DateTimeField('date modified', auto_now=True) 
	completed = models.BooleanField(default=False)

	folder = models.ForeignKey('Folder', verbose_name='folder', null=True)
	

	class Meta:
		app_label = 'tasks'