from rest_framework import serializers
from .models import MyUserManager,MyUser

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"