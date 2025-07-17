from django.shortcuts import render, redirect
from .models import Idea, IdeaStar
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import IdeaForm
from django.http import JsonResponse


# Create your views here.


def ideas_list(request):
    ideas = Idea.objects.all()

    if request.user.is_authenticated:
        starred_idea_ids = IdeaStar.objects.filter(user=request.user).values_list('idea_id', flat=True)
    else:
        starred_idea_ids = []

    return render(request, 'ideas/ideas_list.html', {
        'ideas': ideas,
        'starred_idea_ids': starred_idea_ids
    })


@login_required
def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    user = request.user

    star, created = IdeaStar.objects.get_or_create(user=user, idea=idea)

    if not created:
        # 이미 찜한 상태였으면 취소
        star.delete()

    return redirect('ideas:list')

def ideas_create(request):
    if request.method == 'GET':
        form = IdeaForm()
        context = {
            'form': form
        }
        return render(request, 'ideas/ideas_create.html', context=context)
    else:
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('ideas:list')


def ideas_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    # 로그인 한 사용자일 때만 찜 여부를 체크
    is_starred = False
    if request.user.is_authenticated:
        is_starred = IdeaStar.objects.filter(
            user=request.user,
            idea=idea
        ).exists()

    context = {
        'idea': idea,
        'is_starred': is_starred,
    }
    return render(request, 'ideas/ideas_detail.html', context)

def ideas_delete(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect('/ideas/')

def ideas_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == 'POST':
        # POST 요청이면, 기존 인스턴스에 덮어쓰도록 instance=idea 지정
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:detail', pk=idea.pk)
    else:
        # GET 요청이면, 기존 데이터를 폼에 채워서 보여줌
        form = IdeaForm(instance=idea)

    return render(request, 'ideas/ideas_update.html', {
        'form': form,
        'idea': idea,
    })

def adjust_interest(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    action = request.POST.get('action')
    if action == 'plus':
        idea.interest += 1
    elif action == 'minus':
        idea.interest = max(0, idea.interest - 1)
    else:
        return JsonResponse({'error': 'invalid action'}, status=400)
    idea.save()
    return JsonResponse({'interest': idea.interest})