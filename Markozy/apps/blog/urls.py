from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       url(r'^$', views.PostList.as_view(), name='post-list'),
                       url(r'^(?P<page>\d+)/$', views.PostList.as_view()),
                       url(r'^(?P<slug>[1-9a-z\-]+)/$', views.PostDetail.as_view(), name='post-detail'),
)
