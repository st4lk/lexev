from django.conf import settings
from django.utils.translation import get_language
from haystack.query import SearchQuerySet, DEFAULT_OPERATOR


class MlSearchQuerySet(SearchQuerySet):
    def filter(self, **kwargs):
        """Narrows the search based on certain attributes and the default operator."""
        if 'content' in kwargs:
            kwd = kwargs.pop('content')
            if 'en' in str(get_language()):
                kwdkey = "text"
            else:
                kwdkey = "text_%s" % str(get_language())

            kwargs[kwdkey] = kwd
        if getattr(settings, 'HAYSTACK_DEFAULT_OPERATOR', DEFAULT_OPERATOR) == 'OR':
            return self.filter_or(**kwargs)
        else:
            return self.filter_and(**kwargs)
