# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.utils.feedgenerator import Atom1Feed
import logging

from solid_i18n.urls import solid_i18n_patterns

l = logging.getLogger(settings.DEFAULT_LOGGER)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

from haystack.forms import ModelSearchForm
from haystack.views import SearchView
from utils.custom_search import MlSearchQuerySet

urlpatterns += solid_i18n_patterns('haystack.views',
    url(r'^search/$', SearchView(
        searchqueryset=MlSearchQuerySet(),
        form_class=ModelSearchForm
    ), name='haystack_search_ml'),
)


from articles import views
from articles.feeds import LatestEntries


class LatestEntriesCustom(LatestEntries):
    def title(self):
        if self.link() == '/en/':
            return "Alexey Evseev's blog"
        else:
            return u"Блог Алексея Евсеева"


class LatestEntriesAtomCustom(LatestEntriesCustom):
    feed_type = Atom1Feed

latest_rss = LatestEntriesCustom()
latest_atom = LatestEntriesAtomCustom()

urlpatterns += solid_i18n_patterns('',
    (r'^(?P<year>\d{4})/(?P<month>.{3})/(?P<day>\d{1,2})/(?P<slug>.*)/$', views.redirect_to_article),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/page/(?P<page>\d+)/$', views.display_blog_page, name='articles_in_month_page'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.display_blog_page, name='articles_in_month'),
)

urlpatterns += solid_i18n_patterns('',
    url(r'^$', views.display_blog_page, name='articles_archive'),
    url(r'^page/(?P<page>\d+)/$', views.display_blog_page, name='articles_archive_page'),

    url(r'^tag/(?P<tag>.*)/page/(?P<page>\d+)/$', views.display_blog_page, name='articles_display_tag_page'),
    url(r'^tag/(?P<tag>.*)/$', views.display_blog_page, name='articles_display_tag'),

    url(r'^author/(?P<username>.*)/page/(?P<page>\d+)/$', views.display_blog_page, name='articles_by_author_page'),
    url(r'^author/(?P<username>.*)/$', views.display_blog_page, name='articles_by_author'),

    url(r'^(?P<year>\d{4})/(?P<slug>.*)/$', views.display_article, name='articles_display_article'),

    # AJAX
    url(r'^ajax/tag/autocomplete/$', views.ajax_tag_autocomplete, name='articles_tag_autocomplete'),
)

urlpatterns += i18n_patterns('',
    # RSS
    url(r'^feeds/latest\.rss$', latest_rss, name='articles_rss_feed_latest'),
    url(r'^feeds/latest/$', latest_rss),

    # Atom
    url(r'^feeds/atom/latest\.xml$', latest_atom, name='articles_atom_feed_latest'),
)

# My urls
urlpatterns += solid_i18n_patterns('pages.views',
    url(r'^contacts/$', 'display_about_page', name="contacts")
)

# Sitemap
from myblog.utils.sitemap import sitemaps

urlpatterns += patterns('',
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

if not settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT, 'insecure': True}),
        url(r'^media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT, 'insecure': True}),
    )

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^robots.txt$', 'serve', {
        'path': "/txt/robots.txt",
        'document_root': settings.STATIC_ROOT,
        'insecure': True,
        'show_indexes': False
    }),
)
