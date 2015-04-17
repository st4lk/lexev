# -*- coding: utf-8 -*-
from django.conf import settings
from articles.models import (Article, LANGUAGE_LIST, MARKUP_MARKDOWN,
    MARKUP_REST, MARKUP_TEXTILE, markup)


def do_render_markup(self):
    """
    Turns any markup into HTML
    The same is in articles package + markdown extensions.
    """

    result = False

    for lang in LANGUAGE_LIST:
        content_name = "content_" + lang
        content_value = getattr(self, content_name)
        rendered_content_name = "rendered_content_" + lang
        rendered_content_value = getattr(self, rendered_content_name)
        original = getattr(self, rendered_content_name)

        if self.markup == MARKUP_MARKDOWN:
            setattr(self, rendered_content_name,
                    markup.markdown(content_value, *settings.MARKDOWN_EXTENSIONS))
        elif self.markup == MARKUP_REST:
            setattr(self, rendered_content_name,
                    markup.restructuredtext(content_value))
        elif self.markup == MARKUP_TEXTILE:
            setattr(self, rendered_content_name,
                    markup.textile(content_value))
        else:
            setattr(self, rendered_content_name, content_value)

        if getattr(self, rendered_content_name) != original:
            result = True

    return result


Article.do_render_markup = do_render_markup
