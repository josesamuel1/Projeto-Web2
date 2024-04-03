from rest_framework import serializers
from appEstoque import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'