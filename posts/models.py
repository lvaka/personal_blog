"""Posts Models."""
from django.db import models
from django.utils.text import slugify
from media.models import Media


class Category(models.Model):
    """Category Model to give Posts a Category."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable=False)

    class Meta:
        """How to order category."""

        ordering = ['name']

    def save(self, *args, **kwargs):
        """Slugify before save."""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """Category represented by name."""
        return self.name


class Tag(models.Model):
    """Model for post tags."""

    tagname = models.CharField(max_length=25, unique=True)

    def __str__(self):
        """Tag represented by name."""
        return self.tagname


class Post(models.Model):
    """Blog Post Model."""

    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(editable=False)
    featured = models.ForeignKey(Media,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 related_name='posts')
    publish_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = models.TextField()
    tags = models.ManyToManyField('Tag',
                                  blank=True,
                                  related_name='posts')
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

        ordering = ['-publish_date']

    def __str__(self):
        """Post represented by title and category."""
        return self.title + ' - ' + self.category.name \
            if self.category else self.title
