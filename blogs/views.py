from django.http import HttpResponse
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

# def new(request):

# def create(request):

# def edit(request):


# def update(request):


# def destroy(request):