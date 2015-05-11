from django.shortcuts import render


def home(request):

    template = 'base.html'
    context = {}
    return render(request, template, context)
