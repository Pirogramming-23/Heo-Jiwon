from django.shortcuts import render, redirect
from .models import Idea

# Create your views here.

def ideas_list(request):
    ideas = Idea.objects.all()
    context = {'ideas': ideas}
    return render(request, 'ideas/ideas_list.html', context)

def ideas_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {'idea': idea}
    return render(request, 'ideas/ideas_detail.html', context)