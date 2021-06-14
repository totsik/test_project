from rest_framework.routers import DefaultRouter

from api.view import PostModelView

router = DefaultRouter()
router.register(r'post', PostModelView, basename='api-v1-post')

urlpatterns = [*router.urls]