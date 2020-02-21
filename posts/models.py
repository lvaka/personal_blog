from django.db import models

# Create your models here.
class Category(models.Model):
	"""
		Category Model to give Posts a Category
	"""
	name = models.CharField(max_length=50, unique=True)
	parent = models.ForeignKey('self', 
								on_delete=models.CASCADE, 
								blank=True, 
								null=True,
								related_name='children')
	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Tag(models.Model):
	"""
		Model for post tags
	"""
	tagname = models.CharField(max_length=25, unique=True)
	posts = models.ManyToManyField('Post', 
									related_name='tags')

	def __str__(self):
		return self.tagname

class Post(models.Model):
	"""
		Blog Post Model
	"""
	title = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=160)
	publish_date = models.DateTimeField()
	last_modified = models.DateTimeField(auto_now=True)
	published = models.BooleanField()
	content = models.TextField()
	category = models.ForeignKey('Category', 
								on_delete=models.SET_NULL,
								blank=True,
								null=True,
								related_name='posts')

	class Meta:
		ordering = ['last_modified']

	def __str__(self):
		return self.title + ' - ' + self.category \
					if self.category else self.title