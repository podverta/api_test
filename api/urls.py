from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import PostViewSet, APIComment, APIFollow, APIGroup, \
    MessageViewSet, ClientViewSet, MailViewSet, TagViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('posts/(?P<post_id>[0-9]+)/comments', APIComment,
                basename='comments')
router.register('follow', APIFollow)
router.register('message', MessageViewSet)
router.register('client', ClientViewSet)
router.register('tags', TagViewSet)
router.register('mail', MailViewSet)


urlpatterns = [

    path('group/', APIGroup.as_view()),

]

urlpatterns += router.urls