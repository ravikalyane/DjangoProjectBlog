from django.contrib import admin
from .models import Post, Comment, Message


class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'author', 'created_on', 'status'


class CommentAdmin(admin.ModelAdmin):
    list_display = 'name', 'message', 'post', 'created_on'


class MessageAdmin(admin.ModelAdmin):
    list_display = 'name', 'message', 'message_date'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
