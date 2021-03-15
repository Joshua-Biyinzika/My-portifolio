from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    project = Project.objects.all()

    context = {
        'portifolio_project': project
    }

    return render(request, 'portifolio_app/index.html', context)


def portfolio(request):
    project = Project.objects.all()

    context = {
        'portifolio_project': project
    }

    return render(request, 'portifolio_app/portifolio.html', context)


def portfolio_item_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    context = {
        'project': project,
        'images': images
    }

    return render(request, 'portifolio_app/detail.html', context)


def about(request):
    return render(request, 'portifolio_app/about.html')
