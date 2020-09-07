from django.shortcuts import render,reverse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='user:login')
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        'articles':articles,
    }
    return render(request, 'dashboard.html',context)

@login_required(login_url='user:login')
def add_article(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Your article was created successfully!')
        return redirect('article:dashboard') 
    context = {
        'form':form,
    }
    return render(request, 'add_article.html',context)

def detail(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    context = {
        'article':article,
        'comments':comments,
    }
    return render(request, 'detail.html',context)

@login_required(login_url='user:login')
def update_article(request, id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Your article was created successfully!')
        return redirect('article:dashboard') 
    context = {
        'form':form,
    }
    return render(request, 'update.html',context)

@login_required(login_url='user:login')
def delete_article(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request, "Article deleted successfully")
    return redirect('article:dashboard')

def articles(request):
    keyword = request.GET.get('keyword')

    articles = Article.objects.all()

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)

    context = {
        'articles':articles,
    }
    return render(request, 'articles.html', context)

def add_comment(request,id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        comment_author = request.user
        comment_content = request.POST.get('comment_content')

        new_comment = Comment(comment_author=comment_author, comment_content=comment_content)
        new_comment.article = article
        new_comment.save()
        return redirect(reverse('article:detail', kwargs={'id':id}))