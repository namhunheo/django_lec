from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment, Product
from .forms import CommentForm, MainContentForm, ProductForm

@login_required(login_url='accounts:login')
def maincontent_create(request):
    if request.method == 'POST':
        form = MainContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mysite:index')
    else:
        form = MainContentForm()
    return render(request, 'mysite/maincontent_form.html', {'form': form})

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('mysite:detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('mysite:detail', content_id=comment.content_list.id)

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def detail(request, content_id):
    content = get_object_or_404(MainContent, pk=content_id)
    comments = Comment.objects.filter(content_list=content).order_by('-create_date')
    context = {
        'content': content,
        'comments': comments,
        'form': CommentForm()  # 댓글 생성 폼을 컨텍스트에 추가
    }
    return render(request, 'mysite/content_detail.html', context)

@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('mysite:detail', content_id=content_list.id)
    else:
        form = CommentForm()
    context = {'content_list': content_list, 'form': form}
    return render(request, 'mysite/content_detail.html', context)

@login_required(login_url='accounts:login')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mysite:index')
    else:
        form = ProductForm()
    return render(request, 'mysite/product_form.html', {'form': form})
