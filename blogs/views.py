from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib import auth

from blogs.forms import UserForm
from blogs.models import Blog

def index(request):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    blog_list = Blog.objects.order_by('-published_at')
    return render(request, 'blogs/index.html', {'blog_list': blog_list,})

def show(request, blog_id):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/show.html', {'blog': blog,})

def new(request):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'blogs/new.html', {})

def create(request):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    b = Blog(title=request.POST['blog[title]'],
             content=request.POST['blog[content]'],
             writer=request.POST['blog[writer]'],
             published_at=timezone.now(),
             email=request.POST['blog[email]'])
    b.save()
    return HttpResponseRedirect(reverse('blogs:show', args=(b.id,)))

def edit(request, blog_id):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blogs/edit.html', {'blog': blog})

def update(request, blog_id):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    b = get_object_or_404(Blog, pk=blog_id)
    b.title = request.POST['blog[title]']
    b.content = request.POST['blog[content]']
    b.writer = request.POST['blog[writer]']
    b.email = request.POST['blog[email]']
    b.save()
    return HttpResponseRedirect(reverse('blogs:show', args=(b.id,)))

def destroy(request, blog_id):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    b = get_object_or_404(Blog, pk=blog_id)
    b.delete()
    return HttpResponseRedirect(reverse('blogs:index'))


def logout(request):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect(reverse('login'))
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('blogs:index'))
    registered = False
    user_form = UserForm(data=request.POST)
    if user_form.is_valid():
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        registered = True
    else:
        print user_form.errors
    return render(
            request,
            'blogs/signup.html',
            {'user_form': user_form, 'registered': registered})