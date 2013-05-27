from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
                       url(r'^blog/', include('apps.blog.urls', namespace='blog')),
                       url(r'^admin/', include(admin.site.urls)),
)