"""Media Views."""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from media.models import Media


@login_required
def list_media(request):
    """List all media."""
    media = Media.objects.all()

    for item in media:
        print(item.render_lazyload)

    return render(request, 'media/list.html', {'media': media})
