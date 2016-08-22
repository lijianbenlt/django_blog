from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Blog, Comment
from django import forms


# Create your views here.
def index(request):
    user_list = User.objects.order_by('date_joined')
    context = {
        'user_list': user_list,
    }
    return render(request, 'blog/index.html', context)


def personalinformation(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'User': user,
    }
    return render(request, 'blog/personalinformation.html', context)


def loginpage(request):
    return render(request, 'blog/login.html')


def loginresult(request):
    if request.method == 'POST':
        name = request.POST['name']
        pwd = request.POST['password']
        user = authenticate(username=name, password=pwd)
        if user is not None:
            request.session.set_expiry(0)
            login(request, user)
            # context = {
            #     'User': user,
            #     'Blog_list': Blog.objects.filter(blog_author=user.id)
            # }
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return HttpResponseRedirect(reverse('blog:login'))

    return render_to_response('blog/login.html')


def logoutpage(request):
    logout(request)
    return render(request, 'blog/login.html')


def register(requset):
    return render(requset, 'blog/register.html')


def registerresult(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        pwd = request.POST['password']
        e_mail = request.POST['email']
        user = User.objects.create(username=user_name, first_name=firstname, last_name=lastname, email=e_mail)
        user.set_password(pwd)
        try:
            user.save()
            request.session['user_id'] = user.id
        except Exception:
            pass
        else:
            return HttpResponseRedirect('blog:personalhomepage')


    else:
        return HttpResponseRedirect(reverse('blog:register'))


def personalhomepage(request, home_id):
    request.session['page_id'] = home_id
    user = get_object_or_404(User, pk=home_id)
    blog_list = Blog.objects.filter(blog_author=home_id)
    context = {
        'User': user,
        'Blog_list': blog_list,
        'self': False,
    }
    return render(request, 'blog/personalhomepage.html', context)


def writeblogpage(request):
    user_id = request.session['user_id']
    context = {
        'user_id': user_id,
    }
    # return render(request, 'blog/writeblog.html', context)
    return render(request, 'blog/writeblog.html', context)


def writeblog(request):
    title = request.POST['title']
    content = request.POST['content']
    prvt = request.POST['private']
    pdate = timezone.now()
    author = request.user.id
    blog = Blog.objects.create(blog_title=title, blog_content=content, blog_postdate=pdate,
                               blog_author_id=author, blog_private=prvt)
    try:
        blog.save()
    except Exception:
        # return render(reverse('blog:writeblog', args=[user_id,]))
        return render(reverse('blog:writeblogpage'))
    else:
        context = {
            'blog': blog,
        }
        return render(request, 'blog/viewblog.html', context)


# def deleteblog(request):


def viewblog(request, b_id):
    blog = Blog.objects.get(id=b_id)
    if not blog.blog_private:
        context = {
            'user_id': request.user.id,
            'blog': blog,
        }
        return render(request, 'blog/viewblog.html', context)
    elif not request.user.id == request.session['page_id']:
        raise 404
        return render(request, 'blog/viewblog.html', context)
