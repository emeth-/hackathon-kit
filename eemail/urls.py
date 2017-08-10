from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^catch_all$', "eemail.views.catch_all"),
)
