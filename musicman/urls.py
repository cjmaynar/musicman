from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import Index

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
