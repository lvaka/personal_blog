"""Posts Models."""
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Category Model to give Posts a Category."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        """How to order category."""

        ordering = ['name']

    def __str__(self):
        """Category represented by name."""
        return self.name


class Tag(models.Model):
    """Model for post tags."""

    tagname = models.CharField(max_length=25, unique=True)
    posts = models.ManyToManyField('Post',
                                   related_name='tags')

    def __str__(self):
        """Tag represented by name."""
        return self.tagname


class Post(models.Model):
    """Blog Post Model."""

    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()
    publish_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='posts')

    def save(self, *args, **kwargs):
        """Slugify before save."""
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        """Order by last modified."""

        ordering = ['last_modified']

    def __str__(self):
        """Post represented by title and category."""
        return self.title + ' - ' + self.category \
            if self.category else self.title
