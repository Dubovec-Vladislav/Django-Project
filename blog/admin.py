from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ("id", "title", "slug")
    list_display_links = ("id", "title")


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ("id", "title", "slug")
    list_display_links = ("id", "title")


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    save_as = True
    save_on_top = True

    list_display = ("id", "title", "slug", "author", "category", "created_at", "updated_at", "views", "get_photo")
    list_display_links = ("id", "title", "category",)
    search_fields = ("title", "category",)
    list_filter = ("tags", "category", )

    readonly_fields = ("get_photo", "views", "created_at", "updated_at")
    fields = ("title", "slug", "author", "category", "tags", "content", "photo", "get_photo", "views", "created_at")

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')
        return 'Фото не установлено'

    get_photo.short_description = "Фото"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "comment", "created_at", "updated_at", "post")
    list_display_links = ("id", "name", "comment")
    fields = ("name", "comment", "created_at", "updated_at", "post", "likes")
    readonly_fields = ("created_at", "updated_at",)


class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "comment", "created_at", "updated_at", "parent_comment")
    list_display_links = ("id", "name", "comment")
    fields = ("name", "comment", "created_at", "updated_at", "parent_comment", "likes")
    readonly_fields = ("created_at", "updated_at",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyCommentAdmin)
