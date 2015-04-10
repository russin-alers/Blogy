from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blogy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
    url(r'^addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^page/(\d+)/$','article.views.articles'),
    url(r'^$', 'article.views.articles'),
)
