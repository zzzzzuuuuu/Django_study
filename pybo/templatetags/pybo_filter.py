from django import template

register = template.Library()


@register.filter #템플릿 필터 함수 만들기
def sub(value, arg): #기존값 value, 입력받은 값 arg
    return value - arg