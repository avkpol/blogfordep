
from haystack import indexes
from .models import Entry

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    '''haystack's searchindex object handles data flow into elasticsearch'''

    text     = indexes.CharField(document=True, use_template=True) 
    title    = indexes.CharField(model_attr='title')
    body     = indexes.CharField(model_attr='body')


    def get_model(self):
        
        return Entry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        
        return self.get_model().objects.all()

    



    
    
    