from django.template.base import Library
register = Library()

def listStr(value):
    return str(value[0])

register.filter(listStr)

