from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Category
from .forms import commentForm, postForm, loginForm, registerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def homepage(request):
    posts_objects = Post.objects.order_by("-id")
    categories = Category.objects.all()
    header = 'Blog Web | Blog'
    paginator = Paginator(posts_objects, 2) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts':posts, 'page':page, 'header':header, 'categories':categories})

def single_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    form = commentForm(request.POST)

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False) #because comment has no author, and author cannot be null. Category has already been set.
            comment.post = post
            comment.save()
    # To get Comments
    comments = post.comments.all()
    return render(request, 'single-post.html', {'post': post, 'form': form, 'comments': comments})

@login_required(login_url='/login')
def new_post(request):
    create_post = postForm()
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('/blog')
    return render(request, 'create-post.html', {'newPostForm': create_post})

def login_new(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data#saves in a dictionary
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                if user.is_active:
                    return HttpResponse("Login Successful!")
                else:
                    return HttpResponse("Disabled Account") 
            else:
                return HttpResponse("Login Unsuccessful!")
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    title =  'Create Account'
    form =  registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blog')
    else:
        form = registerForm()
    return render(request, 'signup.html', {'title': title,'form': form})
def info(request):
    title = 'About | Blimp'
    return render(request, 'about.html', {'title': title})
def contact(request):
    title = 'Contact | Blimp'
    return render(request, 'contact.html', {'title': title})
def gallery(request):
    title = 'Gallery | Blimp'
    return render(request, 'gallery.html', {'title': title})

