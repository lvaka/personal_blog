"""Media Model."""
import os
from django.db import models
from django.utils.text import slugify
from media import lib
from django.template.loader import render_to_string


class Media(models.Model):
    """
    Media Model.

        attr:
            filename - name of file
            alt - filename slugified
            full - largest size of image
            mobile - mobile size of image
            prev - tiny ass image for lazy loading
    """

    filename = models.CharField(max_length=155, editable=False)
    alt = models.SlugField(editable=False)
    full = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    full_jpeg = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                                  editable=False)
    mobile = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                               editable=False)
    mobile_jpeg = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                                    editable=False)
    prev = models.ImageField(upload_to='uploads/%Y/%m/%d/',
                             editable=False)

    @property
    def render_lazyload(self):
        """Render lazy load html."""
        media = {
            'id': self.pk,
            'full': self.full.url,
            'full_jpeg': self.full_jpeg.url,
            'mobile': self.mobile.url,
            'mobile_jpeg': self.mobile_jpeg.url,
            'prev': self.prev.url,
            'alt': self.alt
        }
        return render_to_string('media/lazy-load.html', media)

    def handle_images(self):
        """Resize Method."""
        full_img, full_jpeg = lib.resize_by_w(self.full, 1600)
        mobile_img, mobile_jpeg = lib.resize_by_w(self.full, 500)
        prev_img = lib.get_prev(self.full)
        path, ext = os.path.splitext(os.path.basename(self.full.path))
        fullname = '%s.%s' % (path, 'webp')
        fulljpeg = '%s_jpeg.%s' % (path, 'jpg')
        mobilename = '%s-mobile.%s' % (path, 'webp')
        mobilejpeg = '%s-mobile_jpeg.%s' % (path, 'jpg')
        prevname = '%s-prev.%s' % (path, 'jpg')

        self.filename = path
        self.full.save(fullname, full_img, save=False)
        self.full_jpeg.save(fulljpeg, full_jpeg, save=False)
        self.mobile.save(mobilename, mobile_img, save=False)
        self.mobile_jpeg.save(mobilejpeg, mobile_jpeg, save=False)
        self.prev.save(prevname, prev_img, save=False)

    def save(self, *args, **kwargs):
        """Save Override for Media Model."""
        self.alt = slugify(self.filename)
        self.handle_images()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Delete Override for Media Model."""
        del_list = [
            self.full,
            self.full_jpeg,
            self.mobile,
            self.mobile_jpeg,
            self.prev
        ]
        for img in del_list:
            if os.path.exists(img.path):
                os.remove(img.path)

        super().delete(*args, **kwargs)

    def __str__(self):
        """String Representation of Media."""
        return self.filename
