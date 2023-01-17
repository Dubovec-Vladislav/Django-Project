from django import template

register = template.Library()


@register.inclusion_tag('templatetags_templates/sum_of_comments_tpl.html')
def show_sum_of_comments(post):
    comments = post.get_comments.count
    return {"comments": comments}
