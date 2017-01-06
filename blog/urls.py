from django.conf.urls import url
from . import views
from django.conf.urls import url
from . import  views


urlpatterns = {
    url(r'^$', views.post_list, name='post_list'),
    url(r'^search$', views.search_api, name='search_api'),
    url(r'^form$', views.form_action, name='form_action'),
    url(r'^form$', views.form, name='form'),
}