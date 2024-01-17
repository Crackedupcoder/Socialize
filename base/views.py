from django.shortcuts import render,redirect
from .models import Post
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm

def home(request):
    posts = Post.objects.all()
    cxt = {'posts':posts}
    return render(request, 'base/index.html', cxt)


@login_required(login_url='login')
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Post.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


def post_create(request):
    user = request.user

    if request.method == 'POST':
        Post.objects.create(
            user = user,
            text = request.POST.get('text'),
            image = request.FILES.get('image')
        )
        return redirect('home')
    else:
        form = PostCreationForm()
    cxt = {'form':form}
    return render(request, 'base/post_form.html', cxt)