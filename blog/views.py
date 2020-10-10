from django.shortcuts import render, redirect
from .forms import CommentForm, MessageForm
from .models import Post
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MessageForm()
    return render(request, 'index.html', {'form': form})


def post_list(request):
    post = Post.objects.filter(status='Publish').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comment = post.comments.all().order_by('-created_on')
    comment_count = post.comments.all().count()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context = {'post': post, 'form': form, 'comment': comment, 'comment_count': comment_count}
    return render(request, 'post_detail.html', context)


# Category Posts
def python(request):
    post = Post.objects.filter(post_category='Python').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def django(request):
    post = Post.objects.filter(post_category='Django').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def flask(request):
    post = Post.objects.filter(post_category='Flask').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def pyramid(request):
    post = Post.objects.filter(post_category='Pyramid').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def rest_framework(request):
    post = Post.objects.filter(post_category='REST Framework').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def javascript(request):
    post = Post.objects.filter(post_category='Javascript').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def react(request):
    post = Post.objects.filter(post_category='REACT').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def node(request):
    post = Post.objects.filter(post_category='Node').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def angular(request):
    post = Post.objects.filter(post_category='Angular').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def html(request):
    post = Post.objects.filter(post_category='HTML').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def css(request):
    post = Post.objects.filter(post_category='CSS').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def bootstrap(request):
    post = Post.objects.filter(post_category='Bootstrap').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)


def databases(request):
    post = Post.objects.filter(post_category='Databases').order_by('-created_on')
    context = {'post': post}
    return render(request, 'post_list.html', context)
