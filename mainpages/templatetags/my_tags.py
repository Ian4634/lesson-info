from django import template

register = template.Library()


@register.simple_tag
def get_filename(dir):
    list1 = dir.split('/')
    return list1[-1]