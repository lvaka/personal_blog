"""Views for Posts."""
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from posts.models import Post


def post(request, slug):
    """Single post model."""
    post = Post.objects.get(slug=slug)

    return render(request, 'posts/post.html', {'post': post})


def ajax_posts(request):
    """Get Multiple Posts, Return JSON."""
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)

    page = request.GET.get('page')
    page_number = page if page else 1
    page_obj = paginator.get_page(page_number)
    next_page = page_obj.next_page_number() if page_obj.has_next() else None
    next_page = next_page if next_page else ''
    post_list = render_to_string('posts/posts.html', {'page_obj': page_obj})
    json = {'posts': post_list,
            'next_page': next_page}

    return JsonResponse(json)
