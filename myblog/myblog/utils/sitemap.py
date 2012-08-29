from django.contrib.sitemaps import Sitemap
from articles.models import Article
from django.core.urlresolvers import reverse

## articles
class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Article.objects.filter(status__name="Finished")

    def lastmod(self, obj):
        return obj.publish_date

class ArticleEnSitemap(ArticleSitemap):
    def location(self, obj):
        return "/en{0}".format(obj.get_absolute_url()[3:])

class ArticleRuSitemap(ArticleSitemap):
    def location(self, obj):
        return "/ru{0}".format(obj.get_absolute_url()[3:])

## contacts
class ContactsSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [None, ] # just one

class ContactsEnSitemap(ContactsSitemap):
    def location(self, obj):
        return "/en{0}".format(reverse('contacts')[3:])

class ContactsRuSitemap(ContactsSitemap):
    def location(self, obj):
        return "/ru{0}".format(reverse('contacts')[3:])

sitemaps = {
    'articles_en': ArticleEnSitemap(),
    'articles_ru': ArticleRuSitemap(),
    'contacts_en': ContactsEnSitemap(),
    'contacts_ru': ContactsRuSitemap(),
}