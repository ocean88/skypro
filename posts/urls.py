from rest_framework.routers import DefaultRouter
from posts.apps import PostsConfig
from .views import PostViewSet, CommentViewSet

app_name = PostsConfig.name

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [] + router.urls