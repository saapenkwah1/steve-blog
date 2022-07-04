from django.http import Http404
from django.shortcuts import redirect, render
from .models import BlogPost
from .forms import NewBlogForm 
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    items = BlogPost.objects.all()
    context = {'items': items}
    return render(request, 'blogs/index.html',context)


def blogs(request):
    """Show all Blogs"""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """ Displays a Single Blog"""
    blog = BlogPost.objects.get(id = blog_id)
    context = {'blog':blog}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    """Add a new Blog"""
    if request.method != 'POST':
        #No form submitted; create a blank form
        form = NewBlogForm
    else:
        #form is submitted; process data
        form = NewBlogForm(data= request.POST)
        if form.is_valid():
            new_user = form.save(commit =False)
            new_user.owner = request.user
            new_user.save()
            return redirect('blogs:blogs')
    context ={'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request,blog_id):
    """Edit an existing Blog"""
    blog = BlogPost.objects.get(id = blog_id)
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #No edit made
        form = NewBlogForm(instance = blog)
    else:
        #POST data is submitted; Process data
        form = NewBlogForm(instance = blog, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id)
    context = {'blog':blog, 'form':form}
    return render(request, 'blogs/edit_blog.html', context)




    
    







