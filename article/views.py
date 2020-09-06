from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        'articles':articles,
    }
    return render(request, 'dashboard.html',context)

def add_article(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'Your article was created successfully!')
        return redirect('index') 
    context = {
        'form':form,
    }
    return render(request, 'add_article.html',context)

def detail(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    context = {
        'article':article,
    }
    return render(request, 'detail.html',context)