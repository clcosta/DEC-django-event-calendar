import datetime

from django import template

register = template.Library()

@register.filter(name='event_color') 
def event_color(obj):
    lvl = obj.lv_prioridade

    match lvl:
        case 1:
            return "#2E8B57"
        case 2:
            return "#CD853F"
        case 3:
            return "#A52A2A"
        case 4:
            return "#FF0000"

@register.filter(name="sort_by")
def sort_by(obj, order):
    return obj.order_by(order)