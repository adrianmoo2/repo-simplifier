from rest_framework import serializers
from repos.models import Repo

# Repo Serializer
class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = '__all__'