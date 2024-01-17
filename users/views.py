from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from base.models import Post

class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# class UserUpdateView(generic.UpdateView):
#     model = CustomUser
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy('home')
#     template_name = 'users/setting.html'

def user_update_view(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=user)
    cxt = {'form': form}
    return render(request, 'users/setting.html', cxt)


def profile(request, pk):
    user = CustomUser.objects.get(username=pk)
    posts = Post.objects.filter(user=user)
    total_posts = posts.count()
    cxt = {'user':user, 'posts':posts, 'total_posts': total_posts}
    return render(request, 'users/profile.html',cxt)



