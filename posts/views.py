"""Views for Posts."""
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from posts.models import Post, Category


def post(request, slug):
    """Single post model."""
    post = Post.objects.get(slug=slug)

    return render(request, 'posts/post.html', {'post': post})


def ajax_posts(request):
    """Get Multiple Posts, Return JSON."""
    posts = Post.objects.filter(publish_date__isnull=False)
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    page_number = page if page else 1
    page_obj = paginator.get_page(page_number)
    next_page = page_obj.next_page_number() if page_obj.has_next() else None
    next_page = next_page if next_page else ''
    post_list = render_to_string('posts/posts.html', {'page_obj': page_obj})
    json = {'posts': post_list,
            'next_page': next_page}

    return JsonResponse(json)


def ajax_recent_posts(request):
    """Get latest 3 posts."""
    posts = Post.objects.filter(publish_date__isnull=False)[:3]
    post_list = render_to_string('posts/posts-widget-list.html',
                                 {'posts': posts})
    json = {'post_ajax': post_list}

    return JsonResponse(json)


def ajax_categories(request):
    """Get all categories. Return JSON."""
    categories = Category.objects.all()
    cats = []
    for cat in categories:
        cats.append({'category': cat.name,
                     'slug': cat.slug})

    json = {"categories": cats}

    return JsonResponse(json)


def category(request, slug):
    """Category Page view."""
    category = Category.objects.get(slug=slug)

    return render(request,
                  'category/category.html',
                  {'category': category})


def ajax_category_posts(request):
    """Get posts within a category."""
    page = request.GET.get('page')
    category_slug = request.GET.get('category')
    json = {}

    category = Category.objects.get(slug=category_slug)
    if(category):
        posts = category.posts.filter(publish_date__isnull=False)\
                              .order_by('publish_date')
        paginator = Paginator(posts, 5)
        page_number = page if page else 1
        page_obj = paginator.get_page(page_number)
        next_page = ''
        if page_obj.has_next():
            next_page = page_obj.next_page_number()
        post_list = render_to_string('posts/posts.html',
                                     {'page_obj': page_obj})
        json = {'posts': post_list,
                'next_page': next_page}

    return JsonResponse(json)
