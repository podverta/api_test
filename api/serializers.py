from rest_framework import serializers

from .models import Post, Comment, Follow, Group, User, Message, Mail, Client, Tag

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Message

class MailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Mail

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Tag



class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.IntegerField(source='post_id', required=False)
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field='username')
    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following']
            )
        ]

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'id',)
        model = Group