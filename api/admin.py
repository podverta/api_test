from django.contrib import admin
from .models import Post, Comment, Follow, Group, Client, Tag, Message, Mail

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Group)
admin.site.register(Client)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Mail)