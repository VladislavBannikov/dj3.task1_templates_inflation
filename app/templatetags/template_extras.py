from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='float2color')
def float2color(value):
    try:
        value = float(value)
    except ValueError as e:
        return

    if value < 0:
        color = "green"
        result = f' class="{color} "'
    elif 0 <= value < 1:
        return
    else:
        color = 'red'
        if value > 5:
            degree = 1
        elif value > 2:
            degree = 2
        elif value > 1:
            degree = 3
        elif value > 0:
            degree = 4
        else:
            degree = 0
        result = f' class="{color} lighten-{degree}"'
    return mark_safe(result)
