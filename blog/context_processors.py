"""Context Processors."""
from django.conf import settings


def debug(context):
    """Check if template is debug."""
    return {'DEBUG': settings.DEBUG}
