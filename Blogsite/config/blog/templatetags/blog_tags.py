from django import template
from ..models import Category

register = template.Library()
@register.simple_tag
def title():
    return "وبلاگ جنگویی"


@register.inclusion_tag("template_tags/navbar_configuration.html")
def navbar_config():
    catrgories = Category.objects.filter(is_active=True)
    return {
        'categories':catrgories
    }
