from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blogy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),


)
