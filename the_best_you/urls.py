from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts import views as account_views
from home import views as home_views
from blog import views as blog_views
from nutrition import views as nutrition_views
from charts import views as chart_views
from contact import views as contact_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.home, name='home'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # account
    url(r'^register/$', account_views.register, name='register'),
    url(r'^login/$', account_views.login, name='login'),
    url(r'^logout/$', account_views.logout, name='logout'),
    url(r'^profile/$', account_views.profile, name='profile'),
    url(r'^search/$', account_views.get_old_menu, name='get_old_menu'),
    # blog
    url(r'^blog/$', blog_views.post_list, name='post_list'),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),
    url(r'^post/new/$', blog_views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', blog_views.edit_post, name='edit'),
    # nutrition
    url(r'^nutrition/$', nutrition_views.search_name, name='search_name'),
    url(r'^nutrients/(?P<food>\d+)$', nutrition_views.get_nutrients, name='get_nutrients'),
    url(r'^nutrients/post$', nutrition_views.post_nutrients, name='post_nutrients'),
    # chart
    url(r'^chart/data/$', chart_views.get_chart_data, name='get_chart_data'),
    # contact
    url(r'^contact/$', contact_views.contact, name='contact'),
    # Stripe URLS
    url(r'^cancel_subscription/$', account_views.cancel_subscription, name='cancel_subscription'),
]
