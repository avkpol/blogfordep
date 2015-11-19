from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin



urlpatterns = patterns(
    '',
        
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^', include('blog.urls')),
    # url(r'^likes/', include('likes.urls')),
    # (r'^', include('ratings.urls')),
    
)
