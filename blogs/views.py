from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your views here.

from blogs.models import Blog

def index(request):
    blog_list = Blog.objects.order_by('-published_at')
    output = ', '.join([b.title for b in blog_list])
    return HttpResponse(output)

def show(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    output = 'Title: ' + blog.title + ' Content: ' + blog.content + ' Writer: ' + blog.writer + ' Date & Time: ' + str(blog.published_at) + ' Email: ' + blog.email
    return HttpResponse(output)

def new(request):
	return render(request, 'blogs/new.html', {})

def create(request):
	b = Blog(title=request.POST['title'],
			 # content=request.POST['content'],
			 writer=request.POST['writer'],
			 published_at=timezone.now())
	b.save()
	return HttpResponseRedirect(reverse('blogs:show', args=(b.id,)))

# # def edit(request):


# # def update(request):


# # def destroy(request):