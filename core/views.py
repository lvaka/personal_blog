"""Core Views."""
from django.shortcuts import render
from django.core.mail import send_mail
from core.forms import EmailForm


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
