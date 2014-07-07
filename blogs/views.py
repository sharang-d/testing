from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
>>>>>>> c1a8319b6e87588b5ae1f41edb2bfa8e9a580f6d
# Create your views here.

from blogs.models import Blog

def index(request):
    blog_list = Blog.objects.order_by('-published_at')
    output = ', '.join([b.title for b in blog_list])
    template = loader.get_template('blogs/index.html')
    context = RequestContext(request, {
        'blog_list': blog_list,
    })
    return HttpResponse(template.render(context))

def show(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    template = loader.get_template('blogs/show.html')
    context = RequestContext(request, {
        'blog': blog,
    })
    return HttpResponse(template.render(context))

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
