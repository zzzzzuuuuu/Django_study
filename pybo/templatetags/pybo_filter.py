import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter #템플릿 필터 함수 만들기
def sub(value, arg): #기존값 value, 입력받은 값 ag
    return value - arg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))