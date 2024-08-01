from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForms
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_list_detail(request, pk):
    posts = get_object_or_404(Post, id=pk)
    return render(request, 'blog/post_list_detail.html', {'posts': posts})


def post_list_create(request):
    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForms()
    return render(request, 'blog/post_list_form.html', {'form': form})
