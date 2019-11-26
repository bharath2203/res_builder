from django import template

register = template.Library()

@register.filter
def mul_10(value):
  return 10 * value