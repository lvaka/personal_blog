"""Core Views."""
from django.shortcuts import render
from django.core.mail import send_mail
from core.forms import EmailForm
from posts import models


def contact(request):
    """Contact Form."""
    errors = ""
    success = ""

    form = EmailForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            subject = data['subject']
            email = data['email']
            message = data['message']

            try:
                send_mail(
                    "%s from %s" % (subject, name),
                    message,
                    email,
                    ['eric@ericjshin.com'],
                    fail_silently=False
                )
                success = "Email Sent"
            except:
                success = "Couldn't send message"

        else:
            errors = form.errors

    return render(request,
                  'contact/contact.html',
                  {'errors': errors,
                   'message': success})


def xml_sitemap(request):
    """Create an XML Sitemap."""
    posts = models.Post.objects.all()
    latest_post = posts[:1].get()
    categories = models.Category.objects.all()
    tags = models.Tag.objects.all()

    return render(request,
                  'sitemap.xml',
                  {'latest_post': latest_post,
                   'posts': posts,
                   'categories': categories,
                   'tags': tags},
                  content_type="application/xhtml+xml")
