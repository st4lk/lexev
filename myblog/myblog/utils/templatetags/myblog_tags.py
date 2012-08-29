from collections import Iterable
from django import template
register = template.Library()

def sort_as_list( iterable, sort_property):
    """
    Takes an iterable, converts it to list and sorts it by given sort_property
    and returns the list
    """
    if isinstance(iterable, Iterable):
        list_object = list(iterable)
        list_object.sort(key=lambda x:getattr(x, sort_property, None), 
            reverse=True)
        return list_object
    else:
        return None
    
register.filter(sort_as_list)

## django filter examples:
##     django/template/defaultfilters.py 
## django tags examples:
##     django/template/defaulttags.py.