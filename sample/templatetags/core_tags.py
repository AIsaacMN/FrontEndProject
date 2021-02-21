from django import template

register = template.Library()

@register.filter
def private(obj, attribute):
    return getattr(obj, attribute)