"""Views for Posts."""
from django.utils import timezone
from django.db.models import Count
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from posts.models import Post, Category, Tag


def post(request, slug):
    """Single post model."""
    post = Post.objects.get(slug=slug)

    return render(request, 'posts/post.html', {'post': post})


def ajax_posts(request):
    """Get Multiple Posts, Return JSON."""
    today = timezone.now()
    print(today)
    posts = Post.objects.filter(publish_date__isnull=False,
                                publish_date__lte=today)
    print(posts)
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
    today = timezone.now()
    posts = Post.objects.filter(publish_date__isnull=False,
                                publish_date__lte=today)[:3]
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


def ajax_tags(request):
    """Get tags. Return JSON."""
    tags = Tag.objects.annotate(p_count=Count('posts'))\
                      .order_by('-p_count')[:10]
    t_list = []
    for tag in tags:
        t_list.append(tag.tagname)

    json = {"tags": t_list}

    return JsonResponse(json)


def category(request, slug):
    """Category Page view."""
    category = Category.objects.get(slug=slug)

    return render(request,
                  'category/category.html',
                  {'category': category})


def ajax_category_posts(request):
    """Get posts within a category."""
    today = timezone.now()
    page = request.GET.get('page')
    category_slug = request.GET.get('category')
    json = {}

    category = Category.objects.get(slug=category_slug)
    if(category):
        posts = category.posts.filter(publish_date__isnull=False,
                                      publish_date__lte=today)\
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


def tag(request, tag):
    """Tag Page view."""
    tag = Tag.objects.get(tagname=tag)

    return render(request,
                  'tag-posts/tag-posts.html',
                  {'tag': tag})


def ajax_tag_posts(request):
    """Get posts that share the same tag."""
    today = timezone.now()
    page = request.GET.get('page')
    tag_name = request.GET.get('tag')
    json = {}

    tag = Tag.objects.get(tagname=tag_name)
    if(category):
        posts = tag.posts.filter(publish_date__isnull=False,
                                 publish_date__lte=today)\
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
