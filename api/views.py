from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Client, Message, Mail
from .serializers import  (
    MessageSerializer,
    MailSerializer,
    ClientSerializer
)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', ]

class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


