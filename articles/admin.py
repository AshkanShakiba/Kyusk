from django.contrib import admin

from .models import Article, Comment


class CommentStackedInline(admin.StackedInline):
    model = Comment
    extra = 0

class CommentTabularInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentTabularInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
