"""
Media URL Configuration.

    The `urlpatterns` list routes URLs to views. For more
    information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from posts import views

urlpatterns = [
    path('post/<slug:slug>', views.post, name='post'),
    path('', views.ajax_posts, name='posts'),
    path('categories', views.ajax_categories, name='categories ajax'),
    path('tags', views.ajax_tags, name='tags ajax'),
    path('category/<slug:slug>', views.category, name='category'),
    path('tag/<slug:tag>', views.tag, name='tag'),
    path('recent', views.ajax_recent_posts, name='recent posts'),
    path('category-posts', views.ajax_category_posts, name='category posts'),
    path('tag-posts', views.ajax_tag_posts, name='tag posts'),
]
