from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

@login_required
def post_list(request):
    posts = (
        Post.objects.select_related('user')
        .prefetch_related('likes', 'comments__user')
        .order_by('-created_at')
    )
    user_liked_ids = (
        list(request.user.liked_posts.values_list('id', flat=True))
        if request.user.is_authenticated else []
    )
    return render(request, 'posts/post_list.html', {
        'posts': posts,
        'user_liked_ids': user_liked_ids,
    })

@login_required
@require_POST
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post_id in request.user.liked_posts.values_list('id', flat=True):
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'like_count': post.likes.count()})

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    text = request.POST.get('text', '').strip()
    if not text:
        return JsonResponse({'error': 'Empty comment.'}, status=400)
    comment = Comment.objects.create(post=post, user=request.user, text=text)
    return JsonResponse({
        'comment_id': comment.id,
        'username': comment.user.username,
        'text': comment.text
    })

@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden()
    comment.delete()
    return JsonResponse({'success': True})
