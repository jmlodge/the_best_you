from django.conf.urls import url
from django.contrib import admin
from accounts import views as account_views
from home import views as home_views
from blog import views as blog_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.home, name='home'),
    # account
    url(r'^register/$', account_views.register, name='register'),
    url(r'^login/$', account_views.login, name='login'),
    url(r'^logout/$', account_views.logout, name='logout'),
    url(r'^profile/$', account_views.profile, name='profile'),
    # blog
    url(r'^blog/$', blog_views.post_list, name='post_list'),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),
]
