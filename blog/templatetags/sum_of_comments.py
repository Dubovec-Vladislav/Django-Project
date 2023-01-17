from django import template

register = template.Library()


@register.inclusion_tag('templatetags_templates/sum_of_comments_tpl.html')
def show_sum_of_comments(post):
    comments = post.get_comments.count()
    reply_comments = 0
    for comment in post.get_comments.all():
        reply_comments += comment.get_parent_comments.count()
    number_of_comments = comments + reply_comments
    return {"number_of_comments": number_of_comments, }
