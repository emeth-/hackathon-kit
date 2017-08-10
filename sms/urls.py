from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^received$', "sms.views.received"),
)
