from django.db import models
from transmeta import TransMeta
from django.conf import settings
from django.contrib.markup.templatetags import markup

LANGUAGE_LIST = [lang[0] for lang in getattr(settings, 'LANGUAGES')]

class PageClass(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    """
    For single editable from admin interface pages, like 'about' page.
    Markdown is used as default markup.
    """
    __metaclass__ = TransMeta
    title = models.OneToOneField(PageClass)
    content = models.TextField(blank=True)
    markdown_content = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """Renders the page using the appropriate markdown markup."""        
        self.do_render_markup()

        super(Page, self).save(*args, **kwargs)


    def do_render_markup(self):
        """Turns markdown markup into HTML"""

        result = False

        for lang in LANGUAGE_LIST:
            content_name = "content_"+lang
            content_value = getattr(self, content_name)
            rendered_content_name = "markdown_content_"+lang
            rendered_content_value = getattr(self, rendered_content_name)
            original = getattr(self, rendered_content_name)

            setattr(self, rendered_content_name, 
                markup.markdown(content_value))

            if getattr(self, rendered_content_name) != original:
                result = True

        return result

    def __unicode__(self):
        return self.title.name

    class Meta:
        translate = ("content", "markdown_content",)