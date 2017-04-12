from django.conf.urls import url
from django.contrib import admin
from accounts import views as account_views
from home import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.home, name='home'),
    url(r'^register/$', account_views.register, name='register'),
]
