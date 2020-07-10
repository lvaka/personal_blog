"""Media Library."""
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO


def resize_image(image, re_width, width, height, file_format=None):
    """Resize Image."""
    size = (re_width, int(re_width * (height / width)))
    temp_image = image.resize(size, Image.ANTIALIAS)
    temp_file = BytesIO()
    temp_image.save(temp_file, file_format)
    temp_file.seek(0)
    file = ContentFile(temp_file.read())
    return file


def resize_by_w(full, wlimit):
    """Generate full size images."""
    img = Image.open(full)
    img = img.convert(mode="RGB")
    width, height = img.size

    webp = resize_image(img, wlimit, width, height, 'WebP')
    jpeg = resize_image(img, wlimit, width, height, 'JPEG')

    return (webp, jpeg)


def get_prev(full):
    """Generate preview."""
    img = Image.open(full)
    img = img.convert(mode="RGB")
    width, height = img.size

    prev_img = resize_image(img, 100, width, height, 'JPEG')

    return prev_img
