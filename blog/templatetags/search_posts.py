from django import template

register = template.Library()


@register.inclusion_tag('templatetags_templates/search_posts_tpl.html')
def show_search_posts(cnt=4):
    posts = cnt
    return {"posts": posts}
