from django.urls import path
from . import views


app_name = 'blogs'
urlpatterns =[
#Path that leads to home page
    path('', views.index, name = 'index'),

    #Path that displays all blogs
    path('blogs', views.blogs, name='blogs'),

    #Path for a single bog
    path('blog/<int:blog_id>/', views.blog, name ='blog'),
    
    #Path to create new blog
    path('new_blog/', views.new_blog, name = 'new_blog'),

    #Path to edit blog
    path('edit_blog/<int:blog_id>/', views.edit_blog, name= 'edit_blog')
    
]