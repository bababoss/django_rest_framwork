from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^chartJson/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$', views.snippet_detail),
    url(r'^charts/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$',views.index, name = 'index'),
    url(r'^dashboard/$',views.dashboard, name = 'dashboard'),
]