"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
#from blog.views import homepage, single_post, info, contact, gallery, new_post, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', views.homepage),
    #path('blog/<int:post_id>/', views.single_post, name='singlepost'),
    path('blog/<str:post_slug>/', views.single_post, name='singlepost'),
    path('blog/about/', views.info),
    path('blog/contact/', views.contact),
    path('blog/gallery/', views.gallery),
    path('blog/login', views.login_new),
    path('blog/signup', views.register),
    path('blog/create-post', views.new_post)
]
