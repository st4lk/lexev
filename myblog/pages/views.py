from django.shortcuts import render_to_response
from django.template import RequestContext

from pages.models import Page


def display_about_page(request):
    context = {'request': request}

    try:
        about = Page.objects.filter(title__name='about')[0]
    except IndexError:
        about = None

    context["about"] = about

    variables = RequestContext(request, context)
    template = 'pages/contacts.html'
    response = render_to_response(template, variables)
    return response


def display_cv_page(request):
    context = {'request': request}

    try:
        cv = Page.objects.filter(title__name='cv')[0]
    except IndexError:
        cv = None

    context["cv"] = cv

    variables = RequestContext(request, context)
    template = 'pages/cv.html'
    response = render_to_response(template, variables)
    return response
