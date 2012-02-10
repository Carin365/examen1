from django.db import models
class Author(models.Model):
	name = models.CharField(max_length=25)
	lastname = models.CharField(max_length=25)
	birthdate = models.DateField()
	
	def __unicode__(self):
		return 'Author: %s - %s' % (self.pk, self.name,)

class Article(models.Model):
	title = models.CharField(max_length=25)
	author = models.ForeignKey('Author')
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	etiquette = models.ManyToManyField('Etiquette')
	
	def __unicode__(self):
		return 'Article: %s - %s' % (self.pk, self.title,)


class Comment(models.Model):
	article = models.ForeignKey('Article')
	name = models.CharField(max_length=50)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'Comment: %s - %s' % (self.pk, self.name,)

class Etiquette(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return 'Etiquette: %s - %s' % (self.pk, self.name,)
