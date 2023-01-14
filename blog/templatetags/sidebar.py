from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('templatetags_templates/popular_posts_tpl.html')
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('templatetags_templates/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}
