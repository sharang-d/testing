from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from blogs.models import Blog

def index(request):
    blog_list = Blog.objects.order_by('-published_at')
    return render(request, 'blogs/index.html', {'blog_list': blog_list,})

def show(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/show.html', {'blog': blog,})

def new(request):
    return render(request, 'blogs/new.html', {})

def create(request):
    b = Blog(title=request.POST['blog[title]'],
             content=request.POST['blog[content]'],
             writer=request.POST['blog[writer]'],
             published_at=timezone.now(),
             email=request.POST['blog[email]'])
    b.save()
    return HttpResponseRedirect(reverse('blogs:show', args=(b.id,)))

def edit(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blogs/edit.html', {'blog': blog})

def update(request, blog_id):
    b = get_object_or_404(Blog, pk=blog_id)
    b.title = request.POST['blog[title]']
    b.content = request.POST['blog[content]']
    b.writer = request.POST['blog[writer]']
    b.email = request.POST['blog[email]']
    b.save()
    return HttpResponseRedirect(reverse('blogs:show', args=(b.id,)))

def destroy(request, blog_id):
    b = get_object_or_404(Blog, pk=blog_id)
    b.delete()
    return HttpResponseRedirect(reverse('blogs:index'))