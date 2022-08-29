from rest_framework import serializers

from .models import Post, Comment, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.IntegerField(source='post_id', required=False)
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        fields = ('user', 'following',)
        model = Follow

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'id',)
        model = Group