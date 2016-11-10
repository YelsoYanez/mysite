from django.conf.urls import url

from . import views

app_name = 'miafd'
urlpatterns = [
    # ex: /polls/
    url(r'visitors', views.visit, name="visitors"),
    url(r'about', views.about, name="about"),
    url(r'^$', views.index, name="index"),
    url(r'^business/new', views.business_form, name='business_form'),
    url(r'^thanks', views.thanks, name="thanks")
]