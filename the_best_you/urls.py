from django.conf.urls import url
from django.contrib import admin
from accounts import views as account_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', account_views.register, name='register'),
]
