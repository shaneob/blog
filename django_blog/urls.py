from django.conf.urls import patterns, include, url
from blogengine.views import CategoryListView, TagListView, PostsFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tutorial_blog_ng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Blog URLs
    url(r'', include('blogengine.urls')),

    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),

    # Post RSS feed
    url(r'^feeds/posts/$', PostsFeed()),
)

