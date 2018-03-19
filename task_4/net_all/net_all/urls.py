"""net_all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from post import views as post_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signin/$', post_views.signin, name='signin'),
    url(r'^signup/$', post_views.signup, name='signup'),
    url(r'^home', post_views.home, name='home'),
    url(r'^logout/$', post_views.logout_view, name='logout'),
    url(r'^post/(\d+)$', post_views.post, name='post'),
    url(r'^like_click/(\d+)$', post_views.like_click, name='like_click'),
    url(r'^confirm/(.+)$', post_views.confirm, name='confirm'),
    url(r'^confirm_email$', post_views.confirm_email, name='confirm_email'),
]
