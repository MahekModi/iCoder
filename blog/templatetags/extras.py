from django import template

register = template.Library()

@register.filter(name='get_val')
def get_val(dict, key):
    if dict is not None:
        return dict.get(key)
    else:
        pass