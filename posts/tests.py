"""Posts test cases."""
from django.test import TestCase
from posts import models


class TestCategoryTestCase(TestCase):
    """Test Category Model."""

    def setUp(self):
        """Generate Category Instance."""
        cat = models.Category.objects.create(name="Baby")
        cat.save()

    def test_model(self):
        """Testing Model."""
        cat = models.Category.objects.get(name="Baby")
        self.assertEqual(cat.name, "Baby")


class TagTestCase(TestCase):
    """Tag Model Test."""

    def setUp(self):
        """Create Tag."""
        tag = models.Tag.objects.create(tagname='cool')
        tag.save()

    def test_tag(self):
        """Test Tag Model."""
        tag = models.Tag.objects.get(tagname='cool')
        self.assertEqual(tag.tagname, 'cool')


class PostTestCase(TestCase):
    """Test Post Creation."""

    def setUp(self):
        """Post Model."""
        post = models.Post.objects.create(title='Cool Stuff',
                                          content='Really intriguing')
        post.save()

    def test_post(self):
        """Testing Post."""
        post = models.Post.objects.get(title='Cool Stuff')
        self.assertEqual(post.title, 'Cool Stuff')

    def test_slug(self):
        """Testing Post."""
        post = models.Post.objects.get(title='Cool Stuff')
        self.assertEqual(post.slug, 'cool-stuff')
