from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ClientViewSet, MailViewSet

router = DefaultRouter()

router.register('message', MessageViewSet)
router.register('client', ClientViewSet)
router.register('mail', MailViewSet)


urlpatterns = [



]

urlpatterns += router.urls