from django.urls import path, include
from . import views

#we need to set our name of our app here with app_name = 'blog' and the 'blog' will be
#inserted in the all_blogs.html so django knows which app we are using....data coming from
# the blog/urls.py file
app_name = 'blog'

urlpatterns = [
    #the name='all_blogs' is the id name we can use in html code..like in the all_blogs.html file
    path('', views.all_blogs, name='all_blogs'),
    #the name='detail' is the id name so we can use it in html
    # so with the app_name of 'blog' and the name='detail' below in the
    #all_blogs.html we will use it likd <a href="{ url 'blog:detail' blog.id % }"
    # so here we are saying the app_name is blog and the name of the url to get the info from is 'detail'
    path('<int:blog_id>/', views.detail, name='detail'),

]