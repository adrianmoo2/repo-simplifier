from rest_framework import routers
from .api import RepoViewSet

router = routers.DefaultRouter()
router.register('api/repos', RepoViewSet, 'repos')

urlpatterns = router.urls