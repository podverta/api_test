from rest_framework import serializers

from .models import Message, Mail, Client

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Message


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client



class MailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Mail
