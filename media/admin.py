"""Register Media models to admin."""
from django.contrib import admin
from media import models

admin.site.register(models.Media)
