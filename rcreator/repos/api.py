from repos.models import Repo
from rest_framework import viewsets, permissions
from .serializers import RepoSerializer

# Repo Viewset
class RepoViewSet(viewsets.ModelViewSet):
    queryset = Repo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RepoSerializer