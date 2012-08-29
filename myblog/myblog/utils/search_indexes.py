from haystack import indexes
# from django.db import get_model
from articles.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(use_template=True, document=True)
    text_ru = indexes.CharField(use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(status__name="Finished")