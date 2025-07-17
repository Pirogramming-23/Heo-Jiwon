from django.shortcuts import render, redirect
from .models import Tool
from django.shortcuts import get_object_or_404
from ideas.models import Idea

# Create your views here.
def tools_list(request):
    tools = Tool.objects.all()
    context = {'tools': tools}
    return render(request, 'tools/tools_list.html', context)

def tools_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)

    ideas = Idea.objects.filter(devtool=tool)

    return render(request, 'tools/tools_detail.html', {
        'tool':  tool,
        'ideas': ideas,
    })

def tools_create(request):
    if request.method == 'POST':
        Tool.objects.create(
            name = request.POST['name'],
            kind = request.POST['kind'],
            content = request.POST['content'],
        )
        return redirect('/tools/')
    return render(request, 'tools/tools_create.html')

def tools_delete(request, pk):
    if request.method == 'POST':
        tool = Tool.objects.get(id=pk)
        tool.delete()
    return redirect('/tools/')

def tools_update(request, pk):
    tool = Tool.objects.get(id=pk)

    if request.method == 'POST':
        tool.name = request.POST['name']
        tool.kind = request.POST['kind']
        tool.content = request.POST['content']
        tool.save()
        return redirect(f'/tools/{pk}')
    
    context = {'tool': tool}
    return render(request, 'tools/tools_update.html', context)