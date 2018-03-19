import uuid
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from post.models import UserAll, Post, Like, Comments
from net_all import settings


def like_click(request, post_id):
    user = User.objects.get(id=request.user.pk)
    print(user, post_id)
    post = Post.objects.get(id=post_id)
    try:
        like = Like.objects.get(user=user, post_id=int(post_id))
        like.delete()
    except:
        like = Like(post=post, user=user, like=1)
        like.save()
    return redirect('home')


def signin(request):
    context = {'warning': 'User is not found'}
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        name = request.POST.get('Name')
        password = request.POST.get('Password')
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return redirect('confirm_email')
        else:
            return render(request, 'signin.html', context)


def logout_view(request):
    logout(request)
    return redirect('signin')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST.get('Name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        day = request.POST.get('sel_day')
        month = request.POST.get('sel_month')
        year = request.POST.get('sel_year')
        birthday = str(year) + '-' + str(month) + '-' + str(day)
        country = request.POST.get('Country')
        city = request.POST.get('City')
        user = User.objects.create_user(username=user_name, email=email, password=password)
        user.userall = UserAll(city=city, birthday=birthday, country=country, email_confirm=uuid.uuid4().hex)
        user.is_active = False
        user.userall.save()
        user.save()
        user_pass = User.objects.get(username=user_name)
        user_pass = user_pass.userall.email_confirm

        link = '127.0.0.1:8000/confirm/{}'.format(user_pass)
        send_mail('Link for confirming', link, 'toha_livs@meta.ua', [email], fail_silently=False)
        return redirect('confirm_email')


def confirm_email(request):
    user = request.user.pk
    print(user)
    return render(request, 'spasibo.html', {'user': user})


def confirm(request, email_confirm):
    user = UserAll.objects.get(email_confirm=email_confirm)
    user_name = User.objects.get(id=user.user_id)
    print(user_name)
    user_name.is_active = True
    user_name.save()
    return render(request, 'confirm.html', {'user': user_name.username})








def home(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    posts_all = Post.objects.all()
    paginator = Paginator(posts_all, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    #     If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    for post in posts:
        post.num_likes = Like.objects.filter(post=post.id).count()
    context = {'poster': posts, 'posts': posts}
    if request.method == 'GET':
        return render(request, 'home.html', context)
    elif request.method == 'POST':
        search_country = request.POST.get('country')
        search_city = request.POST.get('city')
        posts = Post.objects.filter(country=search_country, city=search_city).all()
        return render(request, 'home.html', {'posts': posts})


def post(request, post_id):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    post = Post.objects.get(id=post_id)
    comm = Comments.objects.filter(post=post_id).all()
    paginator = Paginator(comm, 4)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)
    post.num_likes = Like.objects.filter(post=post_id).count()
    context = {'post': post, 'comm': comm, 'comments': comments}
    if request.method == 'GET':
        return render(request, 'post.html', context)
    if request.method == 'POST':
        return render(request, 'post.html', context)


